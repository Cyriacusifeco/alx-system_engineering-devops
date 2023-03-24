# Kill a process from manifest

exec {'Terminated killmenow':
    command  => 'pkill killmenow',
    provider => 'shell',
}
