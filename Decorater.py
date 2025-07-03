def log_decorator(f):
    def wrapper():
        print("Before function") //first called
        f() //greet called
        print("After function")
    return wrapper

@log_decorator
def greet():
    print("Hello!")

greet()
