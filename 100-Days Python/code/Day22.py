list1 = [1,2,3,4,5]
list2 = ["saurav","kumar"]
print(list1)
print(list2)
# ================================
a = ["saurav",23,"indore","23/07/2005"]
print(a)
# ==================================
print(a[0])
print(a[1])
print(a[2])
# ===============================
print(a[-1])
print(a[-2])
print(a[-3])
# =====================
if "saurav" in a:
    print("Saurav is Present")
else:
    print("IS  Not present")
# ========================================
colors = ["Red","Yellow","blue","Green"]
if "orange" in colors:
    print("Orange is present")
else:
    print("Oranege is absent")


# ======================================================

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:5])
print(animals[5:10])
# ==================================
print(animals[4:])
print(animals[-4:])
# ==================================
print(animals[:-4])
print(animals[:7])
# =================================
print(animals[-1:-9:1])
print(animals[-8:-1:2])
# ================================
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
# =================================================
details = ["Saurav","Kumar","Sharma"]
s = [item for item in details if "a" in item]
print(s)
s = [item for item in details if len(item) < 6]
print(s)
# ===========================================
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)