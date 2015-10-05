#!/usr/bin/env python
'''Usage: junos_port_status.py USER HOST
'''

from docopt import docopt
from junos_lib import *


def port_status(dev):
    ports = PhyPortTable(dev).get()

    print('{}{}{}{}'.format(
        'Interface'.ljust(12),
        'Description'.ljust(40),
        'Status'.ljust(8),
        'Time since last flap'.ljust(45))
    )
    print '-' * 80
    for port in ports:
        if port.description is None:
            port.description = ''
        print('{}{}{}{}'.format(
            port.name.ljust(12),
            port.description.ljust(40),
            port.oper.ljust(8),
            port.flapped.ljust(45))
        )

if __name__ == '__main__':
    args = docopt(__doc__)
    dev = junos_connect(args['USER'], args['HOST'])
    port_status(dev)
