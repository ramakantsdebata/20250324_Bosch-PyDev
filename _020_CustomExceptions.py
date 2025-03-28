class AgeInvalidError(ValueError):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

class AgeMinorError(ValueError):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

def ValidateAge(age):
    try:
        iAge = int(age)
    except ValueError as ex:
        raise TypeError("Invalid type for Age", "030")
    
    if iAge < 0:
        raise AgeInvalidError("Age can't be Negative.", "010")
    elif iAge < 18:
        raise AgeMinorError("Age can't be lower than 18.", "020")
    

###########################################

def Main():
    age = -2
    try:
        # acquired connection 
        ValidateAge(age)
        
    except TypeError as ex:
        print(f"Exception:- {ex!r}")
    finally:
        # release conn
        print("Always executed")


Main()
