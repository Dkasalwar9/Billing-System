iname={1:"tea",2:"coffee",3:"saop",4:"veg oil",5:"hair oil",6:"Brush",7:"T paste",8:"Biscuit",9:"icecream",10:"innerwear",11:"shirt",12:"Jeans",13:"shoes",14:"Body spray",15:"comdom"}
Iprice={1:10,2:20,3:30,4:15,5:12,6:11,7:7,8:9,9:40,10:45,11:40,12:60,13:50,14:70,15:40}
disc={1:12,2:15,3:16,4:10,5:10,6:20,7:45,8:30,9:15,10:25,11:30,12:10,13:15,14:20,15:25}
l=[]
q=[]
print("-"*125)
print("\t\t\t\t\t**Avenue Supermaret**")
print("-"*125)
while True:
    print(""" 
            1.Tea pw             2.Coffee           3.Soap
            4.veg oil            5.hair oil         6.Brush
            7.T paste            8.Biscuit          9.Icecream
            10.Innerwear         11.Shirt           12.Jeans
            13.Shoes             14. Body spray     15.Durex Condom
            """)
    print("-"*125)
    item=int(input("Enter item no  which you want to buy : "))
    quantity=int(input("Enter no of Quantity= "))
    l.append(item)
    q.append(quantity)
    ch=input("Do you want to continue.(y/n)= ")
    sum=0
    if ch=='n':
        print("-"*125)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^18}|".format("Items","Quantity","Price","discount(%)","Total","WD Total"))
        print("-"*125)

        for i in range(len(l)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^18}|".format(iname[l[i]],q[i],Iprice[l[i]],disc[l[i]],q[i]*Iprice[l[i]],(q[i]*Iprice[l[i]])-q[i]*Iprice[l[i]]/100*disc[l[i]]))
            print("-"*125)
            sum=sum+(q[i]*Iprice[l[i]])
        break
print("Total Amount without GST =",sum)
print("Total Amount with GST =",int((10/100)*sum+sum))
print("Thank You !\t Have a Nice day ! \n Visit Again...")