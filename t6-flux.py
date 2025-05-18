team_name = "T6-Flux"
x = 0
y = 0
z = 0
operation = ""
x = int(input("Please Enter the 1st Number: "))
y = int(input("Please Enter the 2st Number: "))
operation = str(input("Please Enter the Desired Operation: "))
if operation == "+":
    z = int(x) + int(y)
elif operation == "-":
    z = int(x) - int(y)
print(f"{x} {operation} {y} = {z}")
