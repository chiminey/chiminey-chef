

# Ensure we have ruby-devel for the postgresql recipe
if platform?("redhat","centos","fedora")
  package "ruby-devel" do
    action :install
  end
  # The basics for Python & devel packages we need for buildout
  mytardis_pkg_deps = [
    "gcc",
    "python-devel"
  ]
end
