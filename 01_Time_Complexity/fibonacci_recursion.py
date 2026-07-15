#time complaxity
def feb(n):
    if n == 1 or n == 0:
        return 1
    else:
        return feb(n-1) +feb(n-2)
    
print(feb(8)) 
    