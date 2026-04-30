def details(name,age,city,mobile):
    print("Hello..")
    print(f'''\n My Name is {name} .\n
            I am {age}. \n
            I am from {city} \n
            You Can contact me : {mobile}
            ''')
    
# details("Saurav",20,"indore",9001005089)

def greet(msg= "Hello"):
    print(msg)
# greet()

# ==================================================
'''Default Argunment'''
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# ===================================================
'''Keyword Argunment'''
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# ==================================================
'''Required arguments'''
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill","Leo")

# =================================================
'''Variable-length arguments'''
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

# ===============================================
'''Keyword Arbitrary Arguments'''
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

# ==================================================
''' return Statement'''
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))