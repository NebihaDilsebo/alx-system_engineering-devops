package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'export_flask_version':
  command     => '/usr/bin/flask --version',
  path        => '/usr/local/bin:/usr/bin:/bin',
  refreshonly => true,
  subscribe   => Package['Flask'],
  notify      => Exec['display_flask_version'],
}

exec { 'display_flask_version':
  command     => '/usr/bin/flask --version',
  path        => '/usr/local/bin:/usr/bin:/bin',
  logoutput   => true,
  refreshonly => true,
}
