marks={"roshani":45,"nikita":67,"nida":96,"laxmi":44,"lavnya":10}
print(marks)

# solution 1 ( sort the dictionary based on values)

sv=sorted(marks.items(),key = lambda x : x[1])
print(sv)


    
# solution 2 (sort only the value)

v=sorted(marks.values())
print(v)