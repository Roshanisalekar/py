# solution 1 using | operator 
dict1={"john": 69, "lisa":96}
dict2={"lisa":94,"anu":56}
print(dict1 | dict2)


# 2 using ** operator 

dict1={"john": 69, "lisa":96}
dict2={"lisa":94,"anu":56}
print({**dict1 ,** dict2})


#using copy () and update()  methods

dict1={"john": 69, "lisa":96}
dict2={"lisa":94,"anu":56}

dict3=dict2.copy()
dict3.update(dict1)

print(dict3)
