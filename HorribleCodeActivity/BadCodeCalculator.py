class Calculator:

    #add A and B if its a #
    def addition(self,A,B):
        if isinstance(A, (int,float)) and isinstance(B, (int, float)):
            return A + B
        else:
            return "not a int or float"

    #subtract A and B if its a #
    def subtract(self,A, B):
        # We don’t trust users, so let’s make sure they input numbers 
        if isinstance(A, (int, float)) and isinstance(B, (int, float)):
            return A - B
        else:
            return "error, input must be a number"  

    #multiply A and B if its a #
    def multiplication(self,A, B):
        if isinstance(A, (int, float)) and isinstance(B, (int, float)):
            return A * B
        else:
            return "not a number"  

    #divide A and B if its a # unless B is 0
    def divide(self,A, B):
        if isinstance(A, (int, float)) and isinstance(B, (int, float)):
            # I don’t know why someone would divide by zero, but just incase
            if B == 0:
                return "error: cannot divide by 0"
            else:
                return A / B
        else:
            return "this is not a valid number" 

# check my code because I obivios can't just google these answers
calc = Calculator()
print(calc.addition(120, 92))       
print(calc.subtract(129, 45))    
print(calc.multiplication(23, 12))  
print(calc.divide(8, 2))          
print(calc.divide(8, 0))      