# manuscript that increase the amount of traffic Nginx server can handle

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
    }

# To restart ngunx and make the settings take effect
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
    }