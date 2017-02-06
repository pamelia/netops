#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.op.phyport import *
from jnpr.junos.utils.config import Config


class Junos(object):
    def __init__(self, username, hostname, port=22):
        self._username = username
        self._hostname = hostname
        self._port = port
        self._dev = Device(user=self._username, host=self._hostname,
                           port=self._port)
        self._dev.open()

    def commit_check(self):
        c = Config(self._dev)
        try:
            c.lock()
            c.commit_check()
            c.unlock()
        except Exception as e:
            print('error: {}'.format(str(e)))

    def port_errors(self):
        return PhyPortErrorTable(self._dev).get()

    def port_status(self):
        return PhyPortTable(self._dev).get()
