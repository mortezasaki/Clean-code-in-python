# Context managers in python


# Method 1
class DBHandler:
    def __enter__(self):
        # do things
        return self
    def __exit__(self, exc_type, ex_value, ex_traceback):
        # do things
        
# Method 2
import contextlib

@contextlib.contextmanager
def db_handler():
     try:
        # do things
        yield
    finally:
        # do things 

# Method 3
# use as decorator
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        # do things
        return self

    def __exit__(self, ext_type, ex_value, ex_traceback):
        # do things

@dbhandler_decorator()
def offline_backup():
     # do things