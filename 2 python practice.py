#assignment operators 
a = 150
b = 100
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a //= b
print(a)


#comparisin operators
a = 150
b = 100
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a != b)

#logical operator
x = 5
y = 10
z = 15

print(x > 0 and y > 5)  

print(x > 10 or z > 10) 

print(not(x > 10))

#members operator
n = "manoj"
l = [2,4,5,7,45,75,67]
print(("m" in n))
print(("z" in n))
print((2 in l))
print(("z" not in n))

#bitwise Operator
a = 6  # In binary: 101
b = 2  # In binary: 011
print(a & b)  
print(a | b)  
print(a ^ b)  
print(~a) 
print(a << 1)  
print(a >> 1)
