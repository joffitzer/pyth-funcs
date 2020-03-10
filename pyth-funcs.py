def say_hi():
    print("Hello User")


print("Top")
say_hi()
print("Bottom")


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")


say_hi("Mike", 53)
say_hi("Steve", 22)


def cube(num):
    return num*num*num


result = (cube(4))

print(result)

