import logging
import sys, os

class CustomFormatter(logging.Formatter):
    def format(self, record):
        """
        The CustomFormatter class is a subclass of the Formatter class. 
        It overrides the format() method of the Formatter class. 
        It adds the func_name_override and file_name_override attributes to the LogRecord object. 
        It then calls the format() method of the Formatter class
        
        Args:
          record: the record to be formatted.
        
        Returns:
          A string.
        """
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)

def logger_init(name: str=None, logdir: str=".", level=logging.INFO):
    """
    Initialize a logger with a stream handler and a file handler
    
    Args:
      name (str): The name of the logger.
      logdir: The directory where the log file will be saved.
      level: The logging level. You can choose from: logging.DEBUG/INFO/WARNING/ERROR/CRITICAL
    
    Returns:
      A logger
    """
    if name is not None:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger()
    
    strfmt = '[%(asctime)s][%(levelname)s][%(filename)s]%(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    formatter = CustomFormatter(fmt=strfmt, datefmt=datefmt)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if logdir is not None:
        os.makedirs(logdir, exist_ok=True)
        if name is not None:
            savepath = os.path.join(logdir, "{}.log".format(name))
        else:
            savepath = os.path.join(logdir, "log")
        file_handler = logging.FileHandler(savepath)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    logger.setLevel(level)
    return logger