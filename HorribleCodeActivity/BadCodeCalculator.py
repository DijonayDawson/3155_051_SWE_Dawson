class Calculator:

    #add A and B if its a #
    def addition(A,B):
        if isinstance(A, (int,float)) and isinstance(B, (int, float)):
            return A + B
        else:
            return "not a int or float"

    
