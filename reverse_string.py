def reverse(str1):
    str = " "
    for i in str1:
        str = i + str
    return str
str1 = "1234abcd"
print("The original string is:",str1)
print("The reverse string is:", reverse(str1)) 