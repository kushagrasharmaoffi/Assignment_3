def string_test(str):
    dict = {"UPPER_CASE" : 0, "LOWER_CASE" : 0}
    for chr in str:
        if chr.isupper():
            dict["UPPER_CASE"] += 1
        elif chr.islower ():
            dict["LOWER_CASE"] += 1
        else:
            pass
    print ("Original String : ", str)
    print ("No. of Uppercase characters : ", dict["UPPER_CASE"])
    print ("No. of Lowercase characters : ", dict["LOWER_CASE"])
string_test('The quick Brow Fox')
