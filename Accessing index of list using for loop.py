# solution 1 using enumerate method
l =[23,45,6 ,7,8]
for index , value in enumerate(l):   #(l,start=1)
    print(index,"-",value)
    
    
# solution 2 using   not enumerate method
l =[23,45,6 ,7,8]
for index in range (len(l)):
    value=l[index]
    print(index,value)
    
    
# accessing value
print(l[3])