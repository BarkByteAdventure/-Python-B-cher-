def helloWorld():
    print("Hello World!")
    
helloWorld()


def addieren(x,y):
    return x + y

x = 10
y = 5

print(addieren(10, 5))


def summe(*zahl):
    summe = 0
    for i in zahl:
        summe += i
    return summe

print(summe(1,2,3))


def funktion():
    variable = 10
    print(variable)
        
funktion()
# print(variable) -> funktioniert nicht hier

