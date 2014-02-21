include_recipe "postgresql::server"

# Probably don't need this, given we have IDENT security
file "/root/postgresql.passwd" do
  content node['postgresql']['password']['postgres']
end

file "/var/tmp/create_chiminey_db.sql" do
  action :create_if_missing
  owner "postgres"
  content <<-EOH
  CREATE USER bdphpc;
  CREATE DATABASE bdphpc OWNER bdphpc;
  EOH
end

bash "create_my_chiminey_db" do
  # previous event-driven version never got triggered for me (SB)
  user "postgres"
  code "psql < /var/tmp/create_chiminey_db.sql"
end
