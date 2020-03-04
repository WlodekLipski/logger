import logging
import logging.config

"""
Logger config filename
"""
filename = 'debug.conf'
logging.config.fileConfig(fname=filename)
log = logging.getLogger()
