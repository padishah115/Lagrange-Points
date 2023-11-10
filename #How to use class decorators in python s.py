#How to use class decorators in python so far

def class_decorator(cls):
    def extra_method(self, value):
        return f"Extra method called with {value}"
    
    cls.extra_method = extra_method

    return cls

def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("THis is executed before the function is called.")
        result = func(*args, **kwargs)
        print("THis is executed after the function has completed running.")
        return result
    return wrapper

@mydecorator
def greet(person):
    print(f"Hello there, {person}!")


person1 = "Hayden"

greet(person1)