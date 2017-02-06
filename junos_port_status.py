#!/usr/bin/env python
"""Usage: junos_port_status.py [--user=<login>] HOST
"""

import os
from docopt import docopt
from junos_lib import Junos


def main():
    args = docopt(__doc__)

    if args['--user']:
        user = args['--user']
    else:
        user = os.environ['USER']

    junos = Junos(user, args['HOST'])
    ports = junos.port_status()

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
    main()
