def convertbinary(n):
    if n>1:
        convertbinary(n//2)
        print(n%2,end="")
print( "the binary of the given number is :")
    
convertbinary(43)