#!/usr/bin/puppet
# this file troubleshoot wrong naming in php file

exec { 'move-wp-locale-file':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin:/usr/local/bin'
}
