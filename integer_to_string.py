#time complaxity log(n)
def intTOstr(i):
    degits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = degits[i%10]+result
        i = i//10
    return result
print(intTOstr(45))