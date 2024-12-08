friends={"roshani":"salekar","nikita":"khilare","nida":"patel","laxmi":"tiwari","lavnya":"sing"}
print(friends)


#solution 1 with .items

for key , value in friends.items():
    print(key,"-",value)
    
# solution 2 with keys

for key in friends:
    print(key)
    
    
#solution 3 with value and key


for key in friends .keys():
    print(key)
    
for i in friends.values():
    print(i)
