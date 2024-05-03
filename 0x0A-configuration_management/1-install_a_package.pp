#installs flask version 2.1.0 from pip3

#first ensure installation of pip3
package { 'python3 pip':
    ensure => 'installed',
}
#Then install flask via pip3
package { 'Flask':
    ensure => '2.1.0',
    provider => 'pip3',
    require => Package['python3-pip'],
}
