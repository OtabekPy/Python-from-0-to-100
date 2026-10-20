
from workers import deliveries



def companyststics(*args,**kwargs):
    total=0
    count=0

    for arg in args:
        for argjon in arg:
            total=total+argjon
            count=count+1

    if count>0:
        average=total/count
    else:
        average=0
    rates=kwargs['rate']

    xx=total*rates
    print(f"The average price is: {average}")
    print(f"The total price is: {xx}")

    print(f"Company name is {kwargs['company_name']}")
    return total,count,average,xx



def deliveiresreport(deliveries,*masofacha, **masofalar):
    masofanijami=0
    report={}
    for value in deliveries.values():
            if value["status"]=="active":
                newf=list(map(lambda x: x*2,value["distances"]))
    for masofani in masofacha:
        for qoshsh in masofani:
            masofanijami+=qoshsh
    minimum = masofalar["minimum"]
    for keysjon,valucha in deliveries.items():
         if valucha["status"]=="active":

             if masofanijami>=minimum:
                    report[keysjon]={
                        "Masofani":masofanijami,
                        "name":valucha["name"],

                    }



    return report

delicha=deliveiresreport(
        deliveries,
        [100, 200],
        [50, 150],
        company_name="Fast Delivery",
        minimum=20
    )
print(delicha)

def highest(deliveries):
    high=0
    highname=None
    found=False
    for key,values in deliveries.items():
        total=0
        if values["status"]=="active":
            total+=values["bonus"]
            if high<total:
                high=total
                highname=values["name"]
                print(f"The highest price is: {total}")
                print(f"The highest bonus is: {high}")
            found=True
    if not found:
        print(f"Not found")
    return highname,high


def filterworkers(deliveries,**kwargs):
   report={}
   minimumof=kwargs["minimum_bonus"]
   found=False
   for keysjon,values in deliveries.items():
           if values["status"]=="active":
               if values["bonus"]>=minimumof:
                   report[keysjon]={
                       "name":values["name"],
                       "bonus":values["bonus"],
                       "status": values["status"],
                   }
                   found=True
   if not found:
       print(f"Not found")


   return report





