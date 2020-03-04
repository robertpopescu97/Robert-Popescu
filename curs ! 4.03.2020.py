print('Citez: "hai sa mergem". Am incheiat citatul')
print ("Hello Wodld \\ Done!")
print ("Ana \n are \n mere") ##  "\n" va crea un alinear noi inaintea cuvintelor
print (" \t Ana  are \n mere")    ## "\t" se foloseste pe post de tab= va pune un spatiu

------------------------------------------------------------------------------------------------------------

## concatenarea aduna doua siruri

print("Hello"+" "+"World")

b = "Hello"
c = "world"
d = "Cursul incepe la ora "
e = " {0} {1} {2} 19:00 " .format(b, c, d,)
print(e)
## avantaj al folosirii acesteia este evitarea concatenari in string

-------------------------------------------------------------------------------------------------------

print(type(b)) ## arata tipul variabilei b

f=2 ## variabila de tip integer
print(str(f)) ##transforma variabila de tip integer in variabila de tip string
print(a*3)  ## multiplica variabila a de 3 ori

-------------------------------------------------------------------------------------------------------------

2/3 ## pentru impartirea folosind "/" se va returna restul
2//3 ## pentru impartirea folosind "//" se va returna catul

--------------------------------------------------------------------------------------------------------------
s = " As manca:"  ## se declara variabilia s ca fiind un string cu textul As manca:
s+= "mere" ## va adauga dupa variabila s declarata mai sus stringul declarat pentru (s+= "mere")
print(s)
## face concaternare=adunare de stringuri

----------------------------------------------------------------------------------------------------------------

g = 2
g+= 3
print(g)
## daca sunt declarate ca variabile de tip integer se va face adunarea

-----------------------------------------------------------------------------------------------------------------

_a  ##  "_" in fata variabilei sunt folosite pentru variabile private
    ## variabila nu poate incepe cu cifra

-----------------------------------------------------------------------------------------------------------------

## if este folosit pentru comparati / pentru conditionari
##

---------------------------------------------------------------------------------------------------------------

a = 3
b = 2
if a>b;
    print ("Variabila a este mai mare")
elif;
    print ("Variabila este egala cu b")
else;
    print ("Variabila este este mai mica decat b")

--------------------------------------------------------------------------
a = input("Valoarea variabilie a este: ")
b = input("Valoarea variabilei b este: ")
if a.isdigit();
    print(a.isdigit())
    print("Valoarea lui a este ()" .format(a))
else;
    print("Te rugam sa introduci un numar")