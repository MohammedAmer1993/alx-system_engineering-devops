#increase the amount of traffic for nginx

#increase the ulimit
exec { 'fix--for-nginx':
    #modify ulimit
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    #path for command
    path    => '/usr/bin/:/bin/'
}

#restart nginx
exec { 'restart-nginx':
    #restart nginx server
    command => '/etc/init.d/nginx restart',
    #path of the command
    path    => '/etc/init.d/'
}
