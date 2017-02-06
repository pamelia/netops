#!/usr/bin/env python
"""Usage: junos_commit_check.py [--user=<login>] HOST
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
    junos.commit_check()


if __name__ == '__main__':
    main()
