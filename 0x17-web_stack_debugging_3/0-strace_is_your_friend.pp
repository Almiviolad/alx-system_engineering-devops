# A puppet to debug by replacing a line on server

$edit_file = '/var/www/html/wp-settings.php'

#replace phpp with php

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edit_file}",
  path    => ['/bin','/usr/bin']
}