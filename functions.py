def square(x):
    return x*x
def area_triangle(base, height):
    return (base*height)

def volume_sphere (radius):
    volume = (4/3) * math.pi * math.pow (radius, 3)
    return volume

x=2
print ("{}**2 = {}".format(x, square(x)))
