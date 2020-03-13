# try:
#     # the program will try to run this first
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     # if the try block throws an error, then this except block will run
#     print("Invalid input")


try:
    # the program will try to run this first
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    # if the try block throws an error, then this except block will run
    print(err)
except ValueError as err:
    print(err)

