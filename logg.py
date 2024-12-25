import logg

logger = logging.getLogger("file_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_info_handler = logging.FileHandler('debug-info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)

warning_error_handler = logging.FileHandler('warning-errors.log')
warning_error_handler.setLevel(logging.WARNING)
warning_error_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warning_error_handler)

logger.debug("Debug massege")
logger.info("Info massege")
logger.warning("Warning massege")
logger.error("Error massege")
logger.critical("Critical massege")