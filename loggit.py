from logger_init import logger_init

import sys, os, functools, inspect, traceback

def loggit(log_args: bool=False, log_res: bool=False, log_time: bool=False):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            func_file = function.__code__.co_filename
            extra_args = {
                "func_name_override": function.__name__,
                "file_name_override": os.path.basename(func_file)
            }
            logger = logger_init()
            
            args_dict = {}
            vars_list = function.__code__.co_varnames[:function.__code__.co_argcount]
            default_list = function.__defaults__
            for i, arg in enumerate(args):
                args_dict[vars_list[i]] = arg
            for key, value in kwargs.items():
                args_dict[key] = value
            for i in range(-1, -len(vars_list) - 1, -1):
                if vars_list[i] not in args_dict.keys():
                    args_dict[vars_list[i]] = default_list[i]
            
            if log_args:
                for i, arg in enumerate(args_dict.keys()):
                    logger.info("[{}][args][{}] {}".format(
                        function.__name__, arg, args_dict[arg]), 
                        extra=extra_args
                    )

            if log_time:
                import time
                start_time = time.time()
                logger.info(
                    "[{}][time-start]".format(function.__name__), 
                    extra=extra_args
                )
                
            res = None
            try:
                res = function(*args, **kwargs)
            except Exception as e:
                logger.error(
                    "[{}] Function raises an error: {}".format(function.__name__, e),
                    extra=extra_args
                )
                for i, arg in enumerate(args_dict.keys()):
                    logger.error("[{}][args][{}] {}".format(
                        function.__name__, arg, args_dict[arg]), 
                        extra=extra_args
                    )
                logger.error(
                    traceback.format_exc(),
                    extra=extra_args
                )

            if log_res:
                logger.info(
                    "[{}] Function returns {}".format(function.__name__, str(res)),
                    extra=extra_args
                )

            if log_time:
                end_time = time.time()
                logger.info(
                    "[{}][time-end]".format(function.__name__), 
                    extra=extra_args
                )
                logger.info(
                    "[{}][time-cost] {:.3f}s".format(function.__name__, end_time - start_time), extra=extra_args
                )
            return res
        return wrapper
    return decorator
