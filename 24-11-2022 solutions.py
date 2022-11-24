
#1.Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
def fuc():
    mylist=[8,2,3,0,7]
    total=0
    for i in range(0,len(mylist)):
        total=total+mylist[i]
    return total
fuc()

#2. Write a function for below scenario. 
#Param has 1000 rupess, ramu contains 5 chocolates, param give 500 rupees to ramu,
#ramu contains 10 chocolates, param give 700 rupees to ramu, 
#ramu contains no chocolates param give 1000 rupees to ramu.
def param_ramu(chocolates):
    if chocolates==5:
        print("param give 500 rupees to ramu")
    elif chocolates==10:
        print("param give 700 rupees to ramu")
    else:
        print("param give 1000 rupees to ramu")
       
param_ramu(0)        

#3.Write a function for below scenario
#Big billon festival in amazon, bill amount on cloths more than 1000 rupess i will get 25% discount on bill.
#bill amount on cloths less than 500 rupess i will get 5% discount on bill.
#bill amount on cloths between 500  to 1000 rupess i will get 20% discount on bill.

def festival_amazon(bill_amount):
    if bill_amount>1000:
        retn=bill_amount-(bill_amount*0.25)
        return retn
    elif bill_amount<500:
        retn=bill_amount-(bill_amount*0.5)
        return retn
    elif bill_amount>=500 or bill_amount<=1000:
        retn=bill_amount-(bill_amount*0.20)
        return retn
festival_amazon(1000)  
               

#3.Write a function for below scenario 
#Big billon festival in amazon, the single formal shirt value is 1500,
#two shirts together buy(1+1 offer) shirts value is 1200
#bulk shirts together buy(1+2 offer) shirts vlaue is 1000
def amazon_festival(shirt):
    if shirt==1:
        print("single formal shirt value is 1500")
    elif shirt==2:
            print("2 shirts value is 1200 1+1 offer")
    elif shirt>2:
            print("3 shirts value is 1000 1+2 offer")
    else:
        print("error in input")
       

amazon_festival(1)

#4.Write a Python program to reverse a string. 
#Sample String : "ramu"
#Expected Output : "umar"
str="ramu"
print(str[-1 :: -1])


#5. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
ourlist = [1,2,3,3,3,3,4,5]
print(set(ourlist))

