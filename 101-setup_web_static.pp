# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
}

# Create necessary directories and files
file { [
  '/data',
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/shared',
  '/data/web_static/releases/test',
]:
  ensure => directory,
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test'],
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
}

# Set ownership of the /data folder
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  require => File['/data/web_static/releases/test/index.html'],
}

# Configure Nginx to serve web_static content
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
    server {
        location /hbnb_static {
            alias /data/web_static/current;
        }
    }
  ',
  notify => Service['nginx'],
  require => Package['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/000-default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx after configuration changes
exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  require => File['/etc/nginx/sites-enabled/000-default'],
}
