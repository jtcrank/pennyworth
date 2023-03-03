import logging
from os.path import expanduser
from os import mkdir

class LogFileHandler(logging.FileHandler):
    def __init__(self, filename):
        path = '~/.pennyworth/logs'
        abs_path = path.replace('~', expanduser('~'), 1)

        super(LogFileHandler, self).__init__(abs_path + '/' + filename)
