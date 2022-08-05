import dns.resolver #import the module
from dns.resolver import NoAnswer, NXDOMAIN, NoNameservers, Timeout
import random
import string
import sys
import subprocess
import os
from datetime import date

listarray = ['cleanwords', 'cleanwords']
listarray = ['cleanwords', 'specialWords']
#listarray = ['cleanwords', 'strangeWords']
#listarray = ['preGenerated', 'preGenerated']
#listarray = [ 'oneWord', 'cleanwords']


addused = open('usedDoamins', 'a+')
usedDoamins = []
blockedWords = []
for usedDoamin in open('usedDoamins', 'r').read().split():
    usedDoamins.append(usedDoamin)
for blockedWord in open('blockedWords', 'r').read().split():
    blockedWords.append(blockedWord)

def wordsLists(x, y):
    list_x = open(x , "r+")
    list_y = open(y , "r+")
    words_list1 = []
    words_list2 = []
    for word in list_x:
        words_list1.append(word.strip())
    for word in list_y:
        words_list2.append(word.strip())
    return random.sample(words_list2, len(words_list2)) , random.sample(words_list2, len(words_list2))
# Generate string random
def randomString(stringLength=3):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def compose(words_list1,words_list2, usedDoamins ,blockedWords):
        try:
            dnss= dns.resolver.Resolver()
            domain = words_list2 + words_list1
            #domain = words_list1 #use a list of domains
            # Adauga string generat random
            # words_list1 += words_list1+randomString(1)
            if domain+'.'+sys.argv[1] in usedDoamins:
                print "Domain used in the past: " + domain+'.'+sys.argv[1]
                #raise
            if words_list1 in blockedWords  or words_list2 in blockedWords:
                print "Domain use BLOCKED WORDS "
                raise
            if words_list1  in words_list2:
                print "Cuvintele corespund"
                raise
            #cut domains cu random
            #domain = domain[0:random.randint(5, int(sys.argv[3]))]

            #cut domains fara random
            #domain = domain[0:int(sys.argv[3])]

            if len(domain) <= int(sys.argv[3]):
                # print 'mare'
                # pass
                domain+= "."+sys.argv[1]
                result = dnss.query(domain, 'NS')
                if result:
                    print  "cumparat: " + domain
                    print >>addused, domain
        except NoAnswer as e:
            print 'NoAnswer good: ' + domain
            print >>addused, domain
            return domain
        except NXDOMAIN as e:
            print 'NXDOMAIN good: ' + domain
            print >>addused, domain
            return domain
        except NoNameservers as e:
            print 'NoNameservers bad: ' + domain
            print >>addused, domain
        except Timeout as e:
            print 'Timeout bad: ' + domain
            print >>addused, domain
        except:
            print "Nu o sa creeze acest domeniu"
buy = []
i = 0
while i < int(sys.argv[2]):
        x = compose(random.choice(wordsLists(listarray[0], listarray[1])[0]), random.choice(wordsLists(listarray[0], listarray[1])[1]) , usedDoamins ,blockedWords)
        if  x is not None:
            buy.append(x)
            i+=1
        # print x + "xasda"


if  buy :
    file = open("to_buy/domains_"+str(len(buy))+sys.argv[1]+date.today().strftime("_%d_%m_%Y"), "a")
    for x in buy:
        print >>file ,x
