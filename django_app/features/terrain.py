# -*- coding: utf-8 -*-

from lettuce import before, after, world
from splinter.browser import Browser
from django.test.utils import setup_test_environment, teardown_test_environment 
from django.core.management import call_command 
import os
import time
import subprocess

@before.all
def initial_setup():
    setup_test_environment()

@after.all
def teardown_environment():
    teardown_test_environment()
