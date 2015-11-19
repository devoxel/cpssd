import sys

class InputError(Exception):
    def __init__(self, value=None):
        self.value = value
    def __str__(self):
        return self.value

def safe_input(func):
    def func_wrapper(*args, **kwargs):
        while True:
            try:
                value = func(*args, **kwargs)
                break
            except KeyboardInterrupt:
                print '\nBye bye'
                sys.exit(0)
            except InputError, e:
                print e
            except:
                print ''
                for value in sys.exc_info():
                    if len(str(value)) > 0: print value
                print 'Something went wrong, please report this!'
        return value
    return func_wrapper

class Prompt(object):
    def __init__(self):
        self.character = '$ '

    @safe_input
    def string_prompt(self, prompt, word_limit):
        value = raw_input(self.character + prompt)
        if word_limit:
            if len(value.split(' ')) > word_limit:
                raise InputError('-> invalid word')
        return value

    @safe_input
    def option_prompt(self, prompt, options):
        value = raw_input(self.character + prompt).lower()
        if value not in options:
            raise InputError('-> invalid option')
        return value
