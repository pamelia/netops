#!/usr/bin/env python
"""Usage: junos_port_errors.py [--user=<login>] HOST
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
    porterrors = junos.port_errors()

    print('{}{}'.format(
        'Interface'.ljust(12),
        'Framing errors'.ljust(40))
    )

    print('-' * 80)

    for pe in porterrors:
        if pe.rx_err_frame > 0:
            print('{}{}'.format(
                pe.name.ljust(12),
                str(pe.rx_err_frame).ljust(40))
            )


if __name__ == '__main__':
    main()
