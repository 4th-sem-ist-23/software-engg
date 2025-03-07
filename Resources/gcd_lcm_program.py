# Finding LCM and HCF

# To Find the HCF use the math module by using the HCF it is possible to find the LCM

# import the math
import math 

# store the number 1
num1 = 12
# store the number 2
num2 = 18

# Find the HCF(GCD) using the gcd method by pass numbers
hcf = math.gcd(num1 , num2)

# Find LCM using formula : LCM = (a * b) / HCF
lcm = (num1 * num2) // hcf # performed the floor division to ignore the decimal value


# Displaying the obtained HCF and LCM
print(f"HCF of {num1} and {num2} is {hcf}")
print(f"LCM of {num1} and {num2} is {lcm}")

"--------------------------------------------------------------------------------------------------"

# Finding the LCM and HCF using the Recursion

def hcf(a , b): # take num1 and num2 as argument
    if b == 0: # check the base condition that b == 0 or not if b == 0 then it returns a
        return a 
    return hcf(b , a % b) # until the base condition is true the b args passed to a and to b reminder of two (a %  b) value is passed

def lcm(a , b):
    # Find LCM using formula : LCM = (a * b) / HCF
    return (a * b) // hcf(a , b) # return the lcm value by formula


num1 = 12
num2 = 18

hcf = hcf(num1 , num2)
# pass the num1 and num2 to hcf function
lcm = lcm(num1 , num2)
# pass the num2 and num2 to lcm function

# Display the both HCF and LCM in formated way
print(f"HCF of the {num1} and {num2} is {hcf}")
print(f"LCM of the {num1} and {num2} is {lcm}")

