"""
def numbers():
    print([1,2,3,4,5,6])


numbers()



def argnum(username, date, age):
    print("%s %s %s" % (username,date,age))

argnum("Jake","50th","27")
"""
"""

def sumnum (a,b):
    return a + b

cat = sumnum(5,50)


print(cat)
"""

"""""
def argument_function(name):
    print("Hi %s, it's nice to meet you!" % (name))

argument_function("Jake")


"""
"""
def numfunction(a,b):
    return a + b

magic = numfunction(50, 100)

print(magic)
"""


# Modify this function to return a list of strings as defined above
def list_benefits():
    return("2","a,","b","c")
    pass

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions" % benefit
    pass

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


