#!/usr/bin/puppet

file {'/etc/ssh/ssh_config':
    ensure => present
}

exec{'adding':
    command => '/usr/bin/echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}

exec{'adding2':
    command => '/usr/bin/echo "PasswordAuthentication no" >> /etc/ssh/ssh_config'
}