
sec=int(input("enter seconds"))
if(sec>=60 and sec<3600):
    mins=sec//60
    secd=sec%60
    print("time is ",mins," minutes and " ,secd, "seconds")
elif(sec>=3600 and sec<86400):
    hour=sec//3600
    remainder=sec%3600
    mins=remainder//60
    secd=remainder%60
    print("time is ",hour,"hours ",mins," minutes and " ,secd, "seconds")
elif(sec>=86400):
    day=sec//86400
    rem=sec%86400
    hour=rem//3600
    rem=rem%3600
    mins=rem//60
    secd=rem%60
    print("time is ",day," day ",hour,"hours ",mins," minutes and " ,secd, "seconds")
else:
    print("time is ",sec," seconds")

