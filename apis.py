#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
JSON API defination
'''



import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(option).
    '''

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

