import inspect

caller = inspect.stack()[1]
caller_frame = caller[0]
caller_globals = caller_frame.f_globals

print(caller_globals)