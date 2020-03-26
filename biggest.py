def biggest(x,y,z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z



print (biggest(3, 6, 9))
#>>> 9

print (biggest(6, 9, 3))
#>>> 9

print (biggest(9, 3, 6))
#>>> 9

print (biggest(3, 3, 9))
#>>> 9

print (biggest(9, 3, 9))
#>>> 9
