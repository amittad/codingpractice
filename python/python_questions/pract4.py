# enter a username and user age and display user is eligible for vote or not

userName = str(input("please enter your name="))
age = int(input("pleaase enter your age="))

if age >= 18:
    print(f"{userName} is eligibale for vote")
elif age < 18 and age >0:
    print(f"{userName} is not eligiable for vote")
else:
    print(f"{userName} please enter a valid age")
