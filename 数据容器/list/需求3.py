list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
my_lisy=[]
my_lisy1=[]
for i in list5:
    if(i>0):
        my_lisy.append(i)
my_lisy1=[i for i in list5 if i<0]
print(my_lisy)
print(my_lisy1)