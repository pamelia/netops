#!/usr/bin/env python
'''Usage: split.py NETWORK SIZE [LIMIT]
'''

import sys
from docopt import docopt
from ipaddress import IPv4Network, IPv6Network


def fail(message):
    print("{}".format(message))
    sys.exit(1)


def main():
    args = docopt(__doc__)

    network = unicode(args['NETWORK'])

    try:
        size = int(args['SIZE'])
    except Exception as e:
        fail(e)

    if args['LIMIT'] is None:
        limit = None
    else:
        limit = int(args['LIMIT'])

    try:
        subnets = IPv4Network(network).subnets(new_prefix=size)
    except Exception as e:
        try:
            subnets = IPv6Network(network).subnets(new_prefix=size)
        except Exception as e:
            fail(e)

    for i, s in enumerate(subnets):
        if limit:
            if i < limit:
                print("{}".format(s.exploded))
            else:
                break
        else:
            print("{}".format(s.exploded))


if __name__ == '__main__':
    main()
