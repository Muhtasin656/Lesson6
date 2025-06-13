height=float(input("enter your height"))
weight=float(input("enter your weight"))
bmi=weight/(height/100)**2
print("your bmi is",bmi)
if bmi<=18.5:
    print(" you are under weight")
elif bmi<=24.5:
    print(" you are healthy")  
elif bmi<=29.9:
    print(" you are over weight")
elif bmi<=34.9:
    print(" you are severely over weight")
elif bmi<=39.9:
    print(" you are obese")
else:
    print("you are severely obese")