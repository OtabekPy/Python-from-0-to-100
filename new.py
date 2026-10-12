students = {
    1: {
        "name": "Ali",
        "age": 20,
        "subjects": ["Python", "SQL"],
        "scores": [85, 90]
    },
    2: {
        "name": "Vali",
        "age": 21,
        "subjects": ["HTML", "Java"],
        "scores": [75, 80]
    }
}
for key, value in students.items():
    print(key,value["name"],value["age"])

def add():
    newid=len(students)+1
    subjects=[]
    scores=[]
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    subjectss = input("Enter your subjects: ")
    subjects.append(subjectss)
    subjectss.split(":")
    scoress = input("Enter your scores separated by comma: ")

    for score in scoress.split(","):
        scores.append(int(score))
    students[newid]={"name":name,"age":age,"subjects":subjects,"scores":scores}
    print(students)
add()
def finds():
    findid=int(input("Enter your ID: "))
    for keys, values in students.items():
        if keys == findid:
            return keys,values
    else:
        print("No such ID")
a=finds()
print(a)


def findaverage():
    idstudents=int(input("Enter your ID: "))
    for keys, values in students.items():
        if keys == idstudents:
            x=values["scores"][0]+values["scores"][1]
            return x/2
    else:
        print("No such ID")
d=findaverage()
print(d)


def addsubjects():

    name=int(input("Enter your ID: "))
    for keys, values in students.items():
        if keys == name:
            subject=input("Enter your subject: ")
            subject.split(",")
            values["subjects"].append(subject)
            return values["subjects"]
    else:
        return "No such ID"

a=addsubjects()
print(a)

def addscores():
    idname=int(input("Enter your ID: "))
    newscores=int(input("Enter your new scores: "))
    for keys, values in students.items():
        if keys == idname:
            values["scores"].append(newscores)
            return values["scores"]
    else:
        return None
scoresall=addscores()
print(scoresall)


def maxscores():
    max_score = 0
    maxname = None

    for keys, values in students.items():
        total = 0

        for score in values["scores"]:
            total += score

        x = total / len(values["scores"])

        if x > max_score:
            max_score = x
            maxname = values["name"]

    return max_score, maxname


maxd = maxscores()
print(maxd)
