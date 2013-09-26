#
# Cookbook Name:: cloudenabling
# Recipe:: default
# Copyright (C) 2012, RMIT University

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.




include_recipe "git"
include_recipe "cloudenabling::build-essential"
include_recipe "cloudenabling::deps"
include_recipe "cloudenabling::nginx"
include_recipe "cloudenabling::postgresql"
include_recipe "redis::install"

# Sadly, only works for centos 6.x for the moment

ohai "reload_passwd" do
   action :nothing
   plugin "passwd"
end

user "bdphpc" do
   action :create
   comment "BDPHPC"
   system true
   home "/home/bdphpc"
   supports :manage_home => true
   notifies :reload, resources(:ohai => "reload_passwd"), :immediately
end

app_dirs = [
  "/opt/cloudenabling",
  "/opt/cloudenabling/shared",
  "/var/lib/cloudenabling",
  "/var/log/cloudenabling",
  "/var/log/cloudenabling/celery",
  "/var/run/cloudenabling",
  "/var/run/cloudenabling/celery",
  "/var/cloudenabling",
  "/var/cloudenabling/remotesys"
]

app_links = {
  "/opt/cloudenabling/shared/data" => "/var/lib/cloudenabling",
  "/opt/cloudenabling/shared/log" => "/var/log/cloudenabling"
}

app_dirs.each do |dir|
  directory dir do
    owner "bdphpc"
    group "bdphpc"
  end
end

app_links.each do |k, v|
  link k do
    to v
    owner "bdphpc"
    group "bdphpc"
  end
end

# setuptools needs to unzip some eggs so needs access this directory
directory "/home/bdphpc/.python-eggs" do
  owner "bdphpc"
  group "bdphpc"
  mode "0770"  
  action :create
end


cookbook_file "/opt/cloudenabling/shared/settings.py" do
  action :create_if_missing
  source "settings.py"
  owner "bdphpc"
  group "bdphpc"
end

cookbook_file "/opt/cloudenabling/shared/buildout.cfg" do
  action :create
  source "buildout.cfg"
  owner "bdphpc"
  group "bdphpc"
end


cookbook_file "/etc/init/celeryd.conf" do
  action :create_if_missing
  source "celeryd.conf"
  mode 0755
  owner "root"
  group "root"
end

cookbook_file "/etc/init/celerybeat.conf" do
  action :create_if_missing
  source "celerybeat.conf"
  mode 0755
  owner "root"
  group "root"
end


cookbook_file "/etc/init/uwsgi.conf" do
  action :create_if_missing
  source "uwsgi.conf"
  owner "bdphpc"
  group "bdphpc"
end

app_symlinks = {}

# if you delete /opt/cloudenabling to regenerate, don't forget to remove
# /var/chef-solo/cache/deploy-revisions/cloudenabling otherwise the respo clone wont work.

# To access private repos, generate ssh key for bdphpc and upload to bitbucket
deploy_revision "cloudenabling" do
  action :deploy
  deploy_to "/opt/cloudenabling"
  repository node['cloudenabling']['repo']
  branch node['cloudenabling']['branch']
  user "bdphpc" 
  group "bdphpc"
  symlink_before_migrate(app_symlinks.merge({
      "log" => "log",
      "buildout.cfg" => "buildout-prod.cfg",
      "settings.py" => "bdphpcprovider/settings.py"
  }))
  purge_before_symlink([])
  create_dirs_before_symlink([])
  symlinks({})
  before_symlink do
    current_release = release_path

    execute "update owner" do
      command "chown -R bdphpc.bdphpc $RELEASEDIR"
      environment ({'RELEASEDIR' => current_release})
    end

    file "/opt/cloudenabling/shared/settings.py" do
      user "bdphpc"
      group "bdphpc"
    end

    file "/opt/cloudenabling/shared/buildout.cfg" do
      user "bdphpc"
      group "bdphpc"
    end

    bash "cloudenabling_buildout_install" do
      user "bdphpc"
      cwd current_release
      code <<-EOH
        # this egg-cache directory never gets created - hopfully not a problem.
        export PYTHON_EGG_CACHE=/opt/cloudenabling/shared/egg-cache
        python setup.py clean
        find . -name '*.py[co]' -delete
        python bootstrap.py -c buildout-prod.cfg -v 1.7.0
        bin/buildout -c buildout-prod.cfg install
        bin/django syncdb --noinput --migrate
        bin/django collectstatic -l --noinput
      EOH
    end
  end
  before_restart do
    # latest versions of uwsgi retrieved from buildout do not support xml
    # so we have to to use earlier version FIXME: use different getting approach
    cookbook_file "/opt/cloudenabling/current/bin/uwsgi" do
       action :create
       mode 0755
       source "uwsgi-old"
       owner "bdphpc"
       group "bdphpc"
    end
  end

  restart_command do
    current_release = release_path

    bash "mytardis_foreman_install_and_restart" do
      cwd "/opt/cloudenabling/current"
      code <<-EOH
        stop uwsgi
        start uwsgi
        service nginx stop
        service nginx stop
        service nginx start
        service redis stop
        service redis start 
        stop celeryd 
        start celeryd
        stop celerybeat 
        start celerybeat 

      EOH
    end
  end
end
