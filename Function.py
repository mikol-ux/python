# def hello():
#     print("hello world")

# hello()

# def add(a=0,b=0):
#     if(type(a) is not int or type(b) is not int):
#         return "enter a number"
#     return a + b
    


# print(add(3,5))
# print(add("name", 2))


# def multiple(*args):
#     print(args)
#     print(type(args))


# multiple(1, 2, 3, 4)

def multi_input(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_input(name="mike", age=24)
