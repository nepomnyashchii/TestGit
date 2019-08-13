"""Write a Python program to convert temperatures to and from celsius, fahrenheit.
 Go to the editor"""


def temp_c(temp):
    c = 5*(temp-32/9)
    return c


print(str(temp_c(1)) + u"фыв")
