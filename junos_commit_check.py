#!/usr/bin/env python
'''Usage: junos_commit_check.py USER HOST
'''

from docopt import docopt
from jnpr.junos.utils.config import Config
from junos_lib import *


def commit_check(dev):
    cu = Config(dev)

    try:
        cu.lock()
        cu.commit_check()
        cu.unlock()
    except Exception as e:
        print('error: {}'.format(str(e)))

    dev.close()


if __name__ == '__main__':
    args = docopt(__doc__)
    dev = junos_connect(args['USER'], args['HOST'])
    commit_check(dev)
