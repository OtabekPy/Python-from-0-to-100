





deliveries = {
    1: {
        "name": "Ali",
        "distances": [2, 5, 8],
        "status": "active",
        "bonus": 10
    },
    2: {
        "name": "Vali",
        "distances": [3, 7, 10],
        "status": "active",
        "bonus": 5
    },
    3: {
        "name": "Sami",
        "distances": [1, 4, 6],
        "status": "inactive",
        "bonus": 0
    }
}
def showsinfo(deliveries):
    for key,value in deliveries.items():
        print(f"ID:{key}/ Name:{value['name']}, Distance:{value['distances']},Status:{value['status']}, Bonus:{value['bonus']}")



def addworker(deliveries):
    x=len(deliveries)+1

    names=input("Enter names:")
    distances=list(map(int,input("Enter distances:").split(",")))
    status=input("Enter status:")
    bonus=int(input("Enter bonus:"))
    deliveries[x]={
        "name": names,
        "distances": distances,
        "status": status,
        "bonus": bonus

    }
    return deliveries


def findss(deliveries):
        id=int(input("Enter ID:"))
        for key,value in deliveries.items():
            if id==key:
                print(f"Name:{value['name']}, Distance:{value['distances']},Status:{value['status']}, Bonus:{value['bonus']}")
                return

        print("Not found")

def  showactive(deliveries):
    found=False
    for key,value in deliveries.items():
        if value["status"]=="active":
            print(f"Name:{value['name']}, Distance:{value['distances']},Bonus:{value['bonus']}")
            found=True
    if not found:
            print(f"Not found")


def deleatesd(deliveries):
    found=False
    deleaf=[]
    id=int(input("Enter ID:"))
    if id in deliveries:
          deliveries.pop(id)
          found=True
    if not found:
        print(f"Not found")

    return deliveries


def updatework(deliveries):
    ids=int(input("Enter the id: "))
    found=False
    for key,value in deliveries.items():
        if ids==key:
            print("1.To Cahge the name: ")
            print("2.To Cahge the status: ")
            print("3.To Cahge the bonus: ")
            choses=input("Enter choice:")
            if choses=="1":
                namef=input("Enter name:")
                value.update({"name":namef})
            elif choses=="2":
                statusf=input("Enter status:")
                value.update({"status":statusf})
            elif choses=="3":
                bonusd=input("Enter bonus:")
                value.update({"bonus":bonusd})
            else:
                print("Invalid choice")
            found=True
    if not found:
        print(f"Not found")

    return deliveries




def delesteworker(deliveries):
    found=False
    inactives=[]
    for key,value in deliveries.items():
        if value["status"]=="inactive":
            inactives.append(key)
            found=True
    for key in inactives:
        deliveries.pop(key)
    if not found:
        print(f"Not found")

    return deliveries
