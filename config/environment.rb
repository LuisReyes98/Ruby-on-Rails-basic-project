# Load the Rails application.
require_relative 'application'

# Initialize the Rails application.
Rails.application.initialize!

Rails.application.configure do
  # Make javascript_pack_tag load assets from webpack-dev-server.
  config.x.webpacker[:dev_server_host] = 'http://localhost:8080'
end