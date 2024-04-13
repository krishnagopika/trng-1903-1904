import sys
try:
    # text = "Hello"
    print(text)

# multile except blocks
except ZeroDivisionError:
    print(" ZeroDivisionError Handled")
except NameError:
    print("NameError Handled")

# handiling multiple errors in single except block
except (NameError, ZeroDivisionError):
    print("Some errors Handled")

else:
    print("text is defined")
finally:
    print("finally")


# exception chaining
def divide(a, b):

    try:
        try:
            c = a/b
            sys.exit()
            print("Hello")
            return f"{c}"
        except NameError:
            print("Name error")
        finally:
            # doesnt re-raise the error
            # return "inner finally block"
            pass   
      
    except ZeroDivisionError as e:
        print(e)
        return "Division by zero"
    finally:
        print("Finally block")

print(type(divide(1,0)))


# user-defined exception
class SampleException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise SampleException("Sample Exception")
except Exception as e:
    print(e)

# raising inbilt exceptions
raise ArithmeticError("Arithemetic error")




