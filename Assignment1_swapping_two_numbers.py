i1=input('enter first element:')
i2=input('enter second element:')
x=float(i1)
y=float(i2)
print('before swapping')
print('x=',x,'y=',y)
temp,x=x,y
y=temp
print('after swapping')
print('x=',x,'y=',y)
