from .debug import log
import time

def somefunc():
    for i in range(0, 10):
        time.sleep(1)
        log.error("I'm there")
        log.warning("I'm there")
        log.info("I'm there")

