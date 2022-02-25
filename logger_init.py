import logging
import sys, os

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)

def logger_init(name: str="", logdir="", level=logging.INFO):
    if name != "":
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
        savepath = os.path.join(logdir, "{}.log".format(name))
        file_handler = logging.FileHandler(savepath)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    logger.setLevel(level)
    return logger