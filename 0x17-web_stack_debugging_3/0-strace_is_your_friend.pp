# Fix php wordpress file
exec { 'fix-wordpress-file':
  command => 'sed -i s/phpp/iphp/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
