import logging
        
logger = logging.getLogger(__name__)
# logger.setLevel(logging.WARNING)
# print(f'Logger={logger.name}')
# print(logger.level)

def stuff():
#     print(f'Handlers={logging.root.handlers}')
#     print(f'Handlers={logger.handlers}')
    logger.debug("module debug msg")
    logger.info("module info msg")
    logger.warning("module warn msg")
    logger.error("module err msg")
    logger.critical("module crit msg")
