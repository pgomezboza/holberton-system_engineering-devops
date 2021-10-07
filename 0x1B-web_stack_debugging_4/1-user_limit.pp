# user limit
file {'/etc/security/limits.conf' :
    ensure => present
}
-> exec { 'user hard limit' :
    command => 'sed -i "/holberton hard/s/5/20000/" /etc/security/limits.conf',
    path    => '/bin'
}
-> exec { 'user soft limit' :
    command => 'sed -i "/holberton soft/s/4/10000/" /etc/security/limits.conf',
    path    => '/bin'
}
