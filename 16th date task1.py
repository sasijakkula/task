# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:34:27 2022

@author: sasij
"""

#Q1: What is the output of the following code?
#var = "James" * 2  * 3
nun = "James" * 2  * 3
nun


#Q2: Create a list (month_lst) with month names and print values  as "this is month of January" 
lst=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
for k in lst:
    sas="this is month of "+k
    print(sas)
   

#Q3: Create a tuple (year_tup) with years from 19470 to 2022
john=[1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]
lst4=[]
for t in john:
    lst4.append(t)
    jump=tuple(lst4)
jump    
    

#Q3: Create a set (flowers_set) with Colors names at least 5 colors names
kamal=["red rose","whait lotus","blue lavender","yellow sunflower","pink rose"]
lst6=[]
for d in kamal:
    lst6.append(d)
    lost=set(lst6)
lost    
    

#Q4: create a dict with your friends names and his/her quality like (funny, intelligent, smart etc)
#ex:ex:  {"friend_name": "Thirish" , "Quality": "Smart"}
dict1={"sravani":"funny" ,"ramya":"intelligent", "navya":"smart"}
dict1




#Q5: Create a dict with family members names and relations
#ex:  {"family_member": "venkatrao" , "relation": "Father"}
dict3={"gandhi":"father","narmada":"mother","sravani":"sister"}
dict3





