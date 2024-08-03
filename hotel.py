def foodie():
    bill=0
    pl=0
    choice=int(input("Enter '1' for CHICKEN BIRYANI\nEnter '2' for CHICKEN LOLLIPOPS\nEnter '3' for CHICKEN 65\nEnter '4' for CHICKEN KABAB\nEnter '5' for KFC CHICKEN\nEnter your choice :"))
    if choice==1:
        print("Cost of one plate is 450")
        plates=int(input("How many plates you want to order :"))
        bill=plates*450
    elif choice==2:
        print("Cost of one plate is 200")
        plates=int(input("How many plates you want to order :"))
        bill=plates*200
    elif choice==3:
        print("Cost of one plate is 250")
        plates=int(input("How many plates you want to order :"))
        bill=plates*250
    elif choice==4:
        print("Cost of one plate is 300")
        plates=int(input("How many plates you want to order :"))
        bill=plates*300
    elif choice==5:
        noofb=input("Enter 'a' for 4 piece-cost 199\nEnter 'b' for 6 piece-cost 399\nEnter 'c' for 10 piece-cost 699 :")
        if noofb=='a':
            pl=int(input("Enter no.of buckets :"))
            bill=199*pl
        elif noofb=='b':
            pl=int(input("Enter no.of buckets :"))
            bill=399*pl
        else:
            pl=int(input("Enter no.of buckets :"))
            bill=699*pl
    else:
        print("Hey youu !!!!\nPlease enter a valid number")
    print("Your bill is ",bill)
    return bill
s=foodie()
total=s

while True:
    again=input("Do you want to order again (yes/no): ").lower()
    if again=="yes":
        q=foodie()
        total+=q
        print("Your total bill is :",total)
    else:
        print("Thankyou for your visiting!!!\nHave ah nice day!!!")
        break


