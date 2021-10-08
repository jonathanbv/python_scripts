#calculating the probability a desired outcome, given several samples taken without replacement
#we will need to define a recursive function

#general probability rule
#p(a or b) = p(a) + p(b) - p(a and b)
#first function is pretty crude...but works
#second function seems to be a solid recursive function (needs error handling)

import fractions

def realFrac(f):
    return "hello"

def genProb(a, b):
    return(a + b - a * b)

def genProbImproved(pop, events):
    if events == 1: return (1/pop)
    return (1/pop) + genProbImproved(pop-1,events-1) - (1/pop) * genProbImproved(pop-1,events-1)

a = (1/30)
b = (1/29)
c = (1/28)
d = (1/27)
e = (1/26)
f = (1/25)
g = (1/24)

print(genProb(a, genProb(b,genProb(c,genProb(d,genProb(e,genProb(f,g)))))))
print(genProbImproved(30,7))
