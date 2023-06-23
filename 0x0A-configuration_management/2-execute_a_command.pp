# kills a process
exec { 'killmenow':
  command  => 'usr/bin/ikillmenow' ,
  provider => [0, 1],
}
