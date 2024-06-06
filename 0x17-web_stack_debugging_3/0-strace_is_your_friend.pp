# this file troubleshoot wrong naming in php file

exec { 'move-wp-locale-file':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  creates => '/var/www/html/wp-includes/class-wp-locale.php',
  cwd     => '/root',
  path    => '/var/www/html/wp-includes/'
}
