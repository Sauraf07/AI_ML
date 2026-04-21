import time
if time.localtime().tm_hour < 12:
    print("Good Morning")
elif time.localtime().tm_hour < 18:
    print("Good Afternoon") 
else:    print("Good Evening")