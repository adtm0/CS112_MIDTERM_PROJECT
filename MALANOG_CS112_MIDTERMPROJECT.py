# Degree/Radian Converter
import math
π = math.pi

print("""DEGREE / RADIAN CONVERTER
      
Convert:                    
1. Radians to Degrees
2. Degrees to Radians
""")

def main():
    user_input = input("Select Conversion: ")
    
    # Convert Radians to Degrees
    if user_input == '1':
        rad_input = input("Enter value in Radians (You may use π):  ")
        deg = rdg(rad_input)
        
        if rad_input == '1' :
            print(f"{rad_input} Radian = {deg} Degrees")
        else:
            print(f"{rad_input} Radians = {deg} Degrees")
        
    # Convert Degrees to Radians
    elif user_input == '2':
        deg_input = eval(input("Enter value in Degrees: "))
        rad = degtorad(deg_input)
        
        if deg_input == 1 :
            print(f"{deg_input} Degree = {rad} Radians")
        else:
            print(f"{deg_input} Degrees = {rad} Radians")
    
    # Prompt user for input again
    else:
        main()
        
def rdg(r):
    
    if r == 'π':
        rad = π
    elif r.__contains__('π'):
        rad = eval(r.strip('π')) * π
    else:
        rad = eval(r)
        
        
    deg =  rad * 180 / π
    
    
    if r.__contains__('π') & bool(rad >= 1):
        return int(deg)
    else:
        return deg.__round__(2)

def degtorad(d):
    
    rad = d * π / 180
    
    if d % 180 == 0:
        
        if d // 180 == 1:
            return π
        else:
            return(f"{d // 180}π")
        
    elif d % 90 == 0:
        
        if d // 90 == 1:
            return("π/2")
        else:
            return(f"{d // 90}π/2") 
        
    elif d % 60 == 0:
        
        if d // 60 == 1:
            return("π/3")
        else:
            return(f"{d // 60}π/3")
        
    elif d % 45 == 0:
        
        if d // 45 == 1:
            return("π/4")
        else:
            return(f"{d // 45}π/4")
        
    elif d % 30 == 0:
        
        if d // 30 == 1:
            return("π/6")
        else:
            return(f"{d // 30}π/6")
         
    else:
        return rad.__round__(2)
    
main()
