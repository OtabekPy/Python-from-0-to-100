class hotel:
    rooms = {
        101: {"price": 150, "booked": False},
        102: {"price": 200, "booked": False},
        103: {"price": 250, "booked": True},
        104: {"price": 300, "booked": True}
    }

    guests = {}
    while True:
        print(f"1.Show all room")
        print(f"2.Book a roomm")
        print(f"3.Show all guests")
        print(f"4.Find a guest")
        print(f"5.Cancell Booking")
        print(f"6.Show avible rooms")
        print(f"7.Calculate Total income")
        print(f"8.Exit")
        num=int(input("Enter your choice: "))
        if num==8:
            break
        elif num==1:
            for keys,values in rooms.items():
                print(keys)
                for key,value in values.items():
                    print(f"{key}: {value}")

        elif num==2:
            user=input("Enter your guest's name: ")
            roomnumber=int(input("Enter your guest's number: "))
            for newkeys,newvalues in rooms.items():
                if roomnumber==newkeys:
                    if not newvalues["booked"]:
                        print("We booked For you ")
                        newvalues["booked"]=True
                        guests[user]={
                            "room":roomnumber,
                            "booked":True
                        }

                    else:
                        print("We booked already")
        elif num==3:
            for keysnames,valuesnames in guests.items():
                print(keysnames,valuesnames)
        elif num==4:
            namegu=input("Enter your guest's name: ")
            for keysnames,valuesnames in guests.items():
                if namegu==keysnames:
                    print(f"{namegu} Booked {valuesnames['room']} Room")

        elif num==5:

            guestname=input("Enter the name: ")
            guestname=guestname.capitalize()
            for keysnames,valuesnames in guests.items():
                if guestname==keysnames:
                    if rooms[valuesnames["room"]]["booked"] == False:
                        print(f"We Cancelled you  room")
                        valuesnames["booked"]=False
                    else:
                        print(f"We did not find")
            else:
                    print(f"{guestname} Not found")

        elif num==6:
            for keysnames,valuesnames in rooms.items():
                if valuesnames["booked"]==False:
                    print(f"Room: {keysnames},Price: {valuesnames['price']}")
                else:
                    print("Other rooms are booked")

        elif num==7:
            total=0
            for keys,values in rooms.items():
                if values["booked"]==True:
                    total += values["price"]
                else:
                    print("The Room is cancelled")
            print(f"Total is: {total} ")


