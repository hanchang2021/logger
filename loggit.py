from logger_init import logger_init

import sys, os, functools, inspect

def loggit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        py_file_caller = inspect.getframeinfo(inspect.stack()[1][0])
        extra_args = { 'func_name_override': function.__name__,
                        'file_name_override': os.path.basename(py_file_caller.filename) }
        logger = logger_init("dock", ".")
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

        for i, arg in enumerate(args_dict.keys()):
            logger.info("[{}][args][{}] {}".format(
                function.__name__, arg, args_dict[arg]), extra=extra_args)
        return function(*args, **kwargs)
    return wrapper