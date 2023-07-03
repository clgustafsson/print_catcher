import sys

class buffering_stdout:
    def __init__(self):
        self.buffer = []

    def write(self, text):
        sys.__stdout__.write(text)
        self.buffer.append(text)

    def flush(self):
        pass

    def close(self):
        pass

    def getbuffer(self):
        return "".join(self.buffer)


def print_catcher(function):
    def wrapper(*args,**kwargs):
        output = buffering_stdout()
        sys.stdout = output
        try:
            result = function(*args,**kwargs)
        finally:
            sys.stdout = sys.__stdout__
        prints = output.getbuffer()

        return result, prints
        
    return wrapper
    
    
@print_catcher
def greet():
    print("Hello world!")

_, out = greet()

print("catched!\n" + out)