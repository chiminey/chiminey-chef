

# Ensure we have ruby-devel for the postgresql recipe
if platform?("redhat","centos","fedora")
  package "ruby-devel" do
    action :install
  end
  # The basics for Python & devel packages we need for buildout
  cloudenabling_pkg_deps = [
    "gcc",
    "python-devel"
  ]
end

cloudenabling_pkg_deps.each do |pkg|
  package pkg do
    action :install
  end
end
