# Using Puppet to make changes to our configuration file
# Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
# Your SSH client configuration must be configured to refuse to authenticate using a password
file_line { 'Set identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
  ensure => present,
  replace => true,
}

file_line { 'Disable password login':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  ensure => present,
  replace => true,
}
