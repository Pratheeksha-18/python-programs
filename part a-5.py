
def nearlyequal(str1,str2):
    if len(str1)!=len(str2):
        print("the length of the 2 strings is different they are not equal")
        return
    count=0
    for ch1,ch2 in zip(str1,str2):
         if ch1!=ch2:
             count+=1
         if count>1:
              print("more than one char is different so the strings are not equal")
              return
    if count==1:
        print("as only one character  is differnt they are nearly equal")
    else:
         print("these strings are equal")
str1=input("enter the string1:")
str2=input("enter the string2:")
nearlyequal(str1,str2)
              
