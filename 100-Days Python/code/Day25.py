countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")    
temp.pop(3)                
temp[2] = "Finland"      
countries = tuple(temp)
print(countries)

# ======================================
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)