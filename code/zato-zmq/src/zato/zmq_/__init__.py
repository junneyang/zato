# -*- coding: utf-8 -*-

"""
Copyright (C) 2016 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# PyZMQ
import zmq.green as zmq

# Zato
from zato.server.connection.connector import Connector

# ################################################################################################################################

class Base(Connector):
    """ Base class for ZeroMQ connections, both channels and outgoing ones, other than Majordomo (MDP).
    """
    def _start(self):
        self.conn = self
        self.ctx = zmq.Context()

    def _send(self, msg, *args, **kwargs):
        raise NotImplementedError('Should be defined in subclasses')

    def _stop(self):
        self.impl.close(50) # TODO: Should be configurable

    def _get_log_details(self, address):
        return '{} {}'.format(self.config.socket_type, address)

    def get_prev_log_details(self):
        return self._get_log_details(self.config.prev_address if 'prev_address' in self.config else self.config.address)

    def get_log_details(self):
        return self._get_log_details(self.config.address)

# ################################################################################################################################
