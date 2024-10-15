import math

# 2-Dimensional area of shapes

def square_area(side):
        return side ** 2

def rectangle_area(length, width):
        return length * width

def trapezoid_area(a, b, height):
        return ((a + b) / 2) * height

def triangle_area(base, height):
        return (base + height) / 2

def triangle_area_trigonometric(a, b, C: float):
        return 0.5 * a * b * math.sin(C)

def circle_area(radius):
        return math.pi * (radius ** 2)

def ellipse_area(l_radius, w_radius):
        return math.pi * l_radius * w_radius

#3-Dimensional surface area of shape formulae

def cube_surface_area(edge_length):
    return 6 * (edge_length ** 2)

def rectangular_prism_surface_area(l, w, h):
    return 2 * ((w * l) + (h * l) + (h * w))

def cylinder_surface_area(radius, height):
       return 2 * math.pi * radius * (radius + height)

def cone_surface_area(radius, slant_height):
       pi = math.pi
       return pi * radius ** 2 + pi * radius * slant_height

def sphere_surface_area(radius):
       return 4 * math.pi * (radius ** 2)

def hemisphere_surface_area(radius):
       return 3 * math.pi * (radius ** 2)

# 3-Dimensional volume of shape formulae

def cube_volume(edge_length):
       return edge_length ** 3

def rectangular_prism_volume(w, h, l):
       return w * h * l

def cylinder_volume(radius, height):
       return math.pi * radius ** 2 * height

def cone_volume(radius, height):
       return math.pi * radius ** 2 * (height / 3)

def sphere_volume(radius):
       return (4 / 3) * math.pi * radius ** 3

def hemisphere_volume(radius): 
       return (2 / 3) * math.pi * radius ** 3

# trigonometric formulae

def cosine_rule_side(b, c, A):
       return (b ** 2 + c ** 2 - 2 * b * c  * math.cos(A)) ** 0.5