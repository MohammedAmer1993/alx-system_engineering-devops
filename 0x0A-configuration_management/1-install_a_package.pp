#!/usr/bin/puppet

#this code will install the package flask
package {'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}