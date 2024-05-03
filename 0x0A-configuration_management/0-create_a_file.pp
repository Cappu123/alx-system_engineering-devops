#Create a file inside a /tmp. having path, permission, owner, grop and content attributes

file {'/tmp':
  path => '/tmp/school',
  owner => 'www-data',
  group => 'www-data',
  content => 'I love Puppet',
}

