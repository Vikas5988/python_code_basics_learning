#Lambda funtion is small function without any name

def double(x):
    return 2*x

double_new=lambda x: 2*x

avg = lambda x,y,z: (x+y+z)/3

print(double(4))

print(double_new(6))

print(avg(40,6,11))