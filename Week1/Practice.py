CustomerInfo="TIm Kate is a prime customer of ABC Inc. He lives in California"
print(CustomerInfo)
print(type(CustomerInfo))

print(len(CustomerInfo))

for c in CustomerInfo:
    print(c)

CustomerList = [ "Tim Kate" , 54 , 6.12 , "Abc Inc" , True]

print(CustomerList)
print(type(CustomerList))

print(CustomerList[1])
print(CustomerList[3])


print(type(CustomerList[1]))
print(type(CustomerList[3]))

CustomerList.append(300000)

print(CustomerList)

CustomerList.insert(1,"Lahore")

print(CustomerList)

CustomerList.remove(54)

CustomerList.pop(0)

print(CustomerList)

print(len(CustomerList))

for x in CustomerList:
    print(x)

CustomerList[0] = "Change vlaue"

print(CustomerList)

customerTuples =  (  "Tim Kate" , 54 , 6.12 , "Abc Inc" , True )

print(customerTuples[0])
print(customerTuples[3])


print(type(customerTuples[0]))

#customerTuples[0] = " Changed value"

CustomerSet = {"Tim Kate" , 54 , 6.12 , "Abc Inc" , True }

print(CustomerSet)
print(type(CustomerSet))
print(len(CustomerSet))

for x in CustomerSet:
    print(x)


CustomerSet.add("Lahore")

print(CustomerSet)


CustomerSet.discard(54)

print(CustomerSet)


customerDictinary = {"name": "Tim Kate" ,"age" : 54 , "height" : 6.12 ,"company": "Abc Inc" , "status" : True }

print(customerDictinary)

print(type(customerDictinary))

customerDictinary["name"]="Tom Kate"

print(customerDictinary["name"] )

customerDictinary["Uiberveristy"] = "Nuces"

print(customerDictinary)

for x in  customerDictinary:
    print ( x)

for x in customerDictinary:
    print(customerDictinary[x])
    