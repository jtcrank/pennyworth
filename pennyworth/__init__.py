# -*- coding: utf-8 -*-

"""Top-level package for Hercules."""

__author__ = """Josh Crank"""
__email__ = 'joshuat.crank@gmailcom'
__version__ = '0.0.1'

import errno
import json
import logging
import logging.config
from os import mkdir
import pkg_resources

from os.path import expanduser, exists as path_exists

from pennyworth.log_file_handler import LogFileHandler

# Set up required directories
if(not path_exists('~/.pennyworth'.replace('~', expanduser('~'), 1))):
    for p in ['~/.pennyworth', '~/.pennyworth/logs', '~/.pennyworth/lists']:
        try:
            mkdir(p.replace('~', expanduser('~'), 1))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            pass

# create logger
log_config = pkg_resources.resource_filename(__name__, 'ext/logger_config.json')
with open(log_config, 'r') as config_file:
    config_dict = json.load(config_file)

logging.handlers.LogFileHandler = LogFileHandler
logging.config.dictConfig(config_dict)
logger = logging.getLogger(__name__)

