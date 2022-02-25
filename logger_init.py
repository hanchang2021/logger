import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)

def init_logger(name: str, save_path: str=""):
    logger = logging.getLogger(name=name)
    if save_path != "":
        file_handler = logging.FileHandler(save_path, 'a+')
        file_handler.setFormatter(CustomFormatter('[%(asctime)s][%(levelname)s][%(filename)s]%(message)s'))
        logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
    
import logging
import sys, os

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)

def logger_init(name: str=None, logdir=None, level=logging.INFO):
    if not name:
        name = __name__
    logger = logging.getLogger(name)
    
    strfmt = '[%(asctime)s][%(levelname)s][%(filename)s]%(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    # formatter = logging.Formatter(strfmt, datefmt)
    formatter = CustomFormatter(fmt=strfmt, datefmt=datefmt)
    # logging.basicConfig(level=level, format=strfmt, datefmt=datefmt)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    # stream_handler.setLevel(level)
    logger.addHandler(stream_handler)

    if logdir is not None:
        os.makedirs(logdir, exist_ok=True)
        savepath = os.path.join(logdir, "{}.log".format(name))
        file_handler = logging.FileHandler(savepath, 'a+')
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(level)
        logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger