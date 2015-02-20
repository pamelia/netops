#!/usr/bin/env python
'''Usage: port_status.py USER HOST
'''

import sys
from docopt import docopt
from jnpr.junos import Device
from jnpr.junos.op.phyport import *


def main():
    args = docopt(__doc__)

    try:
        dev = Device(user=args['USER'], host=args['HOST'])
        dev.open()
    except Exception as e:
        print('unable to connect: {0}'.format(str(e)))
        sys.exit(1)

    ports = PhyPortTable(dev).get()

    print('{0}{1}{2}{3}'.format(
        'Interface'.ljust(12),
        'Description'.ljust(40),
        'Status'.ljust(8),
        'Time since last flap'.ljust(45))
    )
    print '-' * 80
    for port in ports:
        if port.description is None:
            port.description = ''
        print('{0}{1}{2}{3}'.format(
            port.name.ljust(12),
            port.description.ljust(40),
            port.oper.ljust(8),
            port.flapped.ljust(45))
        )


if __name__ == '__main__':
    main()
