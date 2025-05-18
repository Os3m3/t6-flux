team_name = "T6-Flux"


#Decleration:
x = 0
y = 0
z = 0
operation = ""


#Input:

x = int(input("Please Enter the 1st Number: "))
operation = str(input("Please Enter the Desired Operation: "))
y = int(input("Please Enter the 2st Number: "))



#Proccess:
if operation == "+":
    z = int(x) + int(y)

elif operation == "-":
    z = int(x) - int(y)

elif operation =="/":
    z = int(x) / int (y)

elif operation =="**":
    z = int(x) ** int (y)

elif operation =="%":
    z = int(x) % int (y)

elif operation == "*":
    z = int(x) * int(y)

elif operation == "|":
     z = int(x) | int(y)

elif operation == "&":
     z = int(x) & int(y)

elif operation == "^":
     z = int(x) ^ int(y)

#Result:    

print(f"{x} {operation} {y} = {z}")