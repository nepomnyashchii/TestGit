# def myFun(*argv):
#     for arg in argv:
#         if arg!=argv[0]:
#             return "No"
#     else:
#         return ("Yes")
# print(myFun(1,10,1))


# def myFun(*argv):
#     for arg in argv:
#         if arg!=argv[0]:
#             return "No"
#     return "Yes"
# print(myFun(1,1,1))

# par1= 1
# par2 =2
# par3 =3
# par4= 4
# par5 =5
# par6 =6
# par7 =7
# par8 =8
# par9 =9
# par10 =10

# print(data)

def myFun(par1, par2, par3, par4, par5, par6, par7, par8, par9, par10):
    data = [par1, par2, par3, par4, par5, par6, par7, par8, par9, par10]
    for element in data:
        if data[0]!= element:
            return "No"
    return "Yes"
print(myFun(1,2,1,1,1,1,1,1,1,1))
