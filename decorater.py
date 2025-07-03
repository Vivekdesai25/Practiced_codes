def log_decorator(f):
    def wrapper():
        print("Before function")
        f()
        print("After function")
    return wrapper

@log_decorator
def greet():
    print("Hello!")

greet()
