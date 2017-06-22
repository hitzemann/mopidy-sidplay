# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
# import os
# import threading

from mopidy import backend

import pykka

logger = logging.getLogger(__name__)


class SidplayBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config, audio):
        super(SidplayBackend, self).__init__()
        self.config = config
