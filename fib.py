#This function takes a number as input and returns fibonocci number as output 
def fibbonocii(num):
    result = 1
    while num >= 1:
        result = result * (num)
        num = num -1
    return result

num = 3
print(factorial(num))
