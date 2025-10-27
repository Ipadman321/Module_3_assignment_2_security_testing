"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: {Mason Josefchuk}
Date: {Nov-08-2024}
"""
import mortgage

try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2])
                frequency = items[3]

                ### REQUIREMENT:
                ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
                ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
                mortgage_calculation = mortgage(amount, rate, amortization, frequency)

                
                ### REQUIREMENT:
                ### PRINT THE MORTGAGE OBJECT
                print(mortgage_calculation)

            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")

except FileNotFoundError as e:
        print(f"Error produced by: {e}")
