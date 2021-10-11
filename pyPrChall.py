import random
#write a function that takes a single parameter which is a string
#return a list of all indexes that have capital letters

#print indices of capitals in a String
def capitalIndexes(inString):
    outList = list()
    dex = 0
    for char in inString:
        if char.isupper():
            outList.append(inString.index(char, dex)) #look for char, starting at index dex
        dex += 1
    return outList

#print middle char of a String
def mid(inString):
    if len(inString) % 2 == 0:
        return ""
    else:
        return inString[len(inString)//2]

#given dict of form {"Name":"Online|Offline"} print # of online
x = {
"Billy": "online",
"Erica": "online",
"Alan" : "offline"}

def online_count(dict):
    count = 0
    for k, v in dict.items(): #could also do dict[k]
        if v == "online":
            count += 1
    return count

#return a random number between 1-100, inclusive
def random_number():
    return random.randint(1,100)

def only_ints(a, b):
    return type(a) == int and type(b) == int

def double_letters(inString):
    for i in range(len(inString) -1):
        let1 = inString[i]
        let2 = inString[i+1]
        if let1 == let2:
            return True
    return False

#add or remove dots between letters in a string
def add_dots(inString):
    outList = list()
    for dex, char in enumerate(inString):
        outList.append(char)
        if dex == (len(inString) -1):
            break
        elif char.isalpha() and inString[dex+1].isalpha():
            outList.append(".")

    return "".join(outList)
#remove dots between letters. Leave all other dots alone.
def remove_dots(inString):
    outList = list()
    for dex, char in enumerate(inString):
        if char.isalpha() or dex == 0 or dex == (len(inString) - 1):
            outList.append(char)
        elif char == "." and inString[dex - 1].isalpha() and inString[dex + 1].isalpha():
            continue
        else:
            outList.append(char)

    return "".join(outList)

#count sylables in a hypen-delimted word
def syllable_count(inString):
    splitted = inString.split("-")
    print(len(splitted))

#deterimes whether two single words are anagrams
def is_anagram(word_a, word_b):
    if len(word_a) == len(word_b): #first test
        d = dict()
        for char in word_a: #create dict of counts
            if d.get(char):
                continue
            else:
                d[char] = word_a.count(char)
        for char in word_b: #compare counts_b against dict
            if word_b.count(char) != d[char]:
                return False
        return True #return True if all tests are passed
    else:
        return False

def flat(in_list):
    outlist=list()
    for item in in_list:
        try: #Are you an iterable?
            for j in item: #Yes: Iterate my contents
                outlist.append(j)
        except:         #No: Just append me to the list.
            outlist.append(item)
    return outlist
def largest_difference(int_list):
    min = max = None
    for num in int_list:
        if min is None or num < min:
            min = num
        elif max is None or num > max:
            max = num
    return max - min

def div_3(input_int):
    return input_int % 3 == 0

def palindrome(inString):
    #list comprehension approach that I was really proud of
    #rev = "".join([inString[i] for i in range(len(inString) - 1,-1,-1)])
    #return inString == rev

    #smarter approach using string slicing
    return inString == inString[::-1]
print(palindrome('tacocat'))
