# A puppet to replace a line  file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

#replacing line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
