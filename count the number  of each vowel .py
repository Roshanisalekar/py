
# using dictionary 
a = "Harry Potter and the Prisoner of Azkaban"
vowel ="aeiou"
a=a.casefold()
print(a)
count ={} .fromkeys(vowel,0)

for char in a :
    if char in count :
        count[char]+= 1
        
print(count)


# solution 2  using list and dictionary comprehension
a = "Harry Potter and the Prisoner of Azkaban"
vowel ="aeiou"
a=a.casefold()
print(a)
count = {key :sum([1 for char in a if char == key ]) for key in vowel}

print(count)