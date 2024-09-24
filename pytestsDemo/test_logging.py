import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

# logger.addHandler(filehandler) #filehandler object

    filehandler=logging.FileHandler('logfile.log')
    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler) #filehandler object
    logger.setLevel(logging.CRITICAL)

    logger.debug("A debug satement is executed")
    logger.info("information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")