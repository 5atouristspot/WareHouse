# -*- coding: utf-8 -*-

"""
Created on 2017-12-01


@module: gun
@used: gunicorn config
"""

import os
#import gevent.monkey
#gevent.monkey.patch_all()

import multiprocessing

debug = True
loglevel = 'debug'
bind = ':3622'
pidfile = 'backend.pid'
logfile = 'log/gunicorn_debug.log'

#number of run processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'
