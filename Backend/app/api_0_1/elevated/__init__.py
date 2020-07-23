#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2019-4-08


@module: api_0_1/elevated
@used: get  storage info
"""

from flask import Blueprint
api = Blueprint('api_elevated', __name__)

from . import storagebin_info
from . import storagedetail_info
from . import reload_data
from . import storage_utilization_rate

from . import batch_info
from . import batchdetail_info

from . import search_info

__all__ = ['']
__author__ = 'zhihao'