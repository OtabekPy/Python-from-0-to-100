


def calculationsprice(deliveries):
    listmultiple=[]
    for key,value in deliveries.items():
        multiple=list(map(lambda x: x*2,value['distances']))
        listmultiple.append(multiple)
        value["prices"]=listmultiple
    return deliveries

