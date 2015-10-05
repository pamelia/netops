#!/usr/bin/env python

import sys
from jnpr.junos import Device
from jnpr.junos.op.phyport import *


def junos_connect(username, hostname):
    try:
        dev = Device(user=username, host=hostname, port=22)
        dev.open()
    except Exception as e:
        print('unable to connect: {}'.format(str(e)))
        sys.exit(1)
    return dev
