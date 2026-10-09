a =1
# def my_func():
#     a +=1 #error as unresolved reference
#     print(a)
# my_func()


def my_func2():
    global a
    a+=1
    print(a)
my_func2()