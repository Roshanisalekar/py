#solution usind operator

l1=[3,4,5,"a","j","s","l"]
l2=[2,4,9,"s","k","l"]
l3=l1+l2
print(l3)


# solution 2 with  unique value

l1=[3,4,5,"a","j"]
l2=[2,4,9,"s","k","l"]
l12=list(set(l1+l2))
print(l12)

#solution 3 using extend () function
l1 =[3,6,8,2,"a","j"]
l2=[3,6,"k","f","j"]

l1.extend(l2)
print(l1)