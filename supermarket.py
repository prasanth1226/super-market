from datetime  import datetime
name=input("enter the name:")

lists='''
    Rice     Rs 1200/kgs
    suger    Rs 30/per
    salt     Rs 20/per
    oil      Rs 80/liter
    paneer   Rs 110/kg
    maggi    Rs 20/per
    Boost    Rs 40/each
    colgate  Rs 20/each
    '''
price=0
pricelist=[]
totalprice=0
Finalfinalamount=0
ilist=[]
qlist=[]
plist=[]

items={'Rice':20,'sugar':30,'salt':20,'oil':80,'maggi':110,'Boost':20,'colgate':20}    #{key :value}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want buy press 1 or 2 for exist:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter the items:")
        quantity=int(input("Enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item, quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you items are not avalibe")
    else:
        print("you items is worng")         
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
         pass
         if finalamount!=0:
             print(25*"=","prasanth supermarket",25*"=")
             print(28*" ","khammam")
             print("Name:",name,30*" ","date:",datetime.now())
             print(75*"_")
             print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
             for i in range(len(pricelist)):
                 print(i,8*" ",5*" ",ilist[i],3*" ",3*" ",qlist[i],8*" ",plist[i])
                 print(75*"=")
                 print(50*" ",'totalAmount:','Rs',totalprice)
                 print("gstamount:",40*" ",'Rs',gst)
                 print(75*" ")
                 print(50*" ","finalamount:",'Rs',finalamount)
                 print(75*"_")
                 print(80*" ", 'Thanks for  visiting')
                 print(75*" ") 
       