companies = {
    1: {
        "name": "TechPro",
        "city": "Riga",
        "income": [50000, 60000, 45000],
        "expenses": [20000, 25000, 15000],
        "employees": [
            {"name": "Ali", "salary": 2500},
            {"name": "Vali", "salary": 3000}
        ]
    }
}
def addnewdict(**kwargs):
    x=len(companies)+1
    companies[x] = kwargs
addnewdict(name="Swisscom",city="Riga",income=[22000, 33000, 33000],expenses=[1000, 9000, 3000],employees=[ {"name": "Ali", "salary": 2500},
            {"name": "Vali", "salary": 3000}])
addnewdict(name="Apple",city="Riga",income=[77000, 23000, 13000],expenses=[700, 800, 3000],employees=[ {"name": "Otabek", "salary": 2500},
            {"name": "Xurshid", "salary": 3000}])




def shows():
    for key,value in companies.items():
        print(key)
        print(value["name"],value["city"])


def newcompany():
    x=len(companies)+1
    income=[]
    expense=[]
    employess={}
    names=input("Enter your name of company:  ")
    cities=input("Enter your city of company:  ")
    incomes=input("Enter your income of company,by ,:  ")
    incomes.split(",")
    income.append(incomes)
    expenses=input("Enter your expense of company,by ,:  ")
    expenses.split(",")
    expense.append(expenses)
    employ=input("Enter your employee name :  ")
    employess["name"]=employ
    employesalary=int(input("Enter your employee salary :  "))
    employess["salary"]=employesalary

    companies[x]={
        "name": names,
        "city": cities,
        "income": income,
        "expenses": expense,
        "employees": employess

    }





def findbyID():
    ids=int(input("Enter your ID of company:  "))
    for keys,values in companies.items():
        if ids==keys:
            print(keys,values)
    else:
        print("There is none")




def findprofits():
    idk=int(input("Enter your ID of company:  "))
    for keys,values in companies.items():
            totalincome=0
            totalexpense=0
            if idk==keys:
                for profits in values["income"]:
                    totalincome+=profits
                for expensecomp in values["expenses"]:
                    totalexpense+=expensecomp

                print(f"total income is {totalincome}")
                print(f"total expense is {totalexpense}")
                print(f"Tottal profit is {totalexpense-totalincome}")
    else:
            print("There is none")


def findriches():
    richest=0
    richestname=None
    for keys,values in companies.items():
        totalincomes=0
        totalexpenses=0
        for valuesss in values["income"]:
            totalincomes+=valuesss
        for valueexpenses in values["expenses"]:
            totalexpenses+=valueexpenses

        x=totalincomes-totalexpenses

        if x>richest:
            richest=x
            richestname=values["name"]


    return richestname,richest







def findemployess():
    employessd=0
    namecompany=None
    for keys,values in companies.items():
        totalemloyee=0
        for valuesss in values["employees"]:
            totalemloyee+=1

        if totalemloyee>employessd:
            employessd=totalemloyee
            namecompany=values["name"]
    return employessd,namecompany


while True:
    print("---COMPANY MANAGMENT-------")
    print("1.Show all companies")
    print("2. Add a new company")
    print("3. Find a company")
    print("4. Calculate company profit")
    print("5.Find the richest company by profit")
    print("6. Find company with the most employees")
    print("7. Find company with the highest total employee salary")
    print("8.Exit")

    enters=int(input("Enter your choice:  "))
    if enters==8:
        break
    elif enters==1:
        shows()
    elif enters==2:
        newcompany()
    elif enters==3:
        findbyID()
    elif enters==4:
        findprofits()
    elif enters==5:
        aa = findriches()
        print(aa)
    elif enters==6:
        findemplo = findemployess()
        print(findemplo)






