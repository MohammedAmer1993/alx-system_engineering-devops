#!/usr/bin/puppet
# puppet bash to edit ssh_config file
file {'/etc/ssh/ssh_config':
    ensure => present
}

exec{'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'

}

exec{'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config'

}