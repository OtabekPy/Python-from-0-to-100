from workers import deliveries, showsinfo, addworker,findss,showactive,deleatesd,delesteworker
from calculations import *
from report import companyststics,highest,filterworkers

while True:
    print("Welcome to the Main Project")

    print("1. Show all workers")
    print("2. Add worker")
    print("3. Find worker")
    print("4. Show active workers")
    print("5. Delete worker")
    print("6. Calculate prices")
    print("7. Company statistics")
    print("8. Highest bonus worker")
    print("9. Filter workers by bonus")
    print("10. Delete inactive workers")
    print("0. Exit")
    ids = int(input("Please enter your Choices: "))
    if ids == 0:
        break
    elif ids == 1:
        showsinfo(deliveries)
    elif ids == 2:
        ads=addworker(deliveries)
        print(ads)
    elif ids == 3:
        ff=findss(deliveries)
        print(ff)
    elif ids == 4:
         active=showactive(deliveries)
         print(active)
    elif ids == 5:
        dels=deleatesd(deliveries)
        print(dels)
    elif ids == 6:
        calcul=calculationsprice(deliveries)
        print(calcul)
    elif ids == 7:
        aa = companyststics(
            [100, 300, 200],
            [50, 150],
            company_name="Fast Delivery",
            rate=2
        )
        print(aa)
    elif ids == 8:
        aa = highest(deliveries)
        print(aa)

    elif ids==9:
        result = filterworkers(
            deliveries,
            minimum_bonus=10
        )
        print(result)
    elif ids==10:
        adel=delesteworker(deliveries)
        print(adel)