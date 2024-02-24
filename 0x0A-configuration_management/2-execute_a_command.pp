#!/usr/bin/puppet



exec {'killmenow':
    command => '/usr/bin/pkill killmenow',
    onlyif  => '/usr/bin/pgrep -l killmenow',
}