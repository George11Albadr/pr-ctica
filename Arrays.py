debits=[]
credits=[]
conteoc=0
conteod=0
print("1. Ingrese el debito")
print("2. Ingrese el credito")
print("3. Total de debitos")
print("4. Total creditos")
print("5. Saldo")
print("6. Promedio de debitos")
print("7. Promedio creditos")
print("8. Monto de debitos mas grande")
print("9. Conteo de operaciones")
print("10. Mostrar todos los creditos y debitos")
print("11. Eliminar creditos")
print("12. Salir")
 
i=0
while i != 12:
        
    i=int(input("Ingrese Su opcion correspondiente al numero:"))
    if i == 1:
        debits.append(int(input("Ingrese el debito:")))
        conteod=conteod+1
    if i == 2:
        credits.append(int(input("Ingrese el credito:")))
        conteoc=conteoc+1
    if i == 3:
        derr=0
        for j in debits:
            derr=derr+j    
        print("Total debitos",derr)
    if i == 4:
        derr=0
        for j in credits:
            derr=derr+j
        print("Total creditos",derr)
    if i == 5:
        derr=0
        for j in credits:
            derr=derr+j
        for j in debits:
            derr=derr+j
        print("Saldo",derr)
    if i == 6:
        conteor=0
        derr=0
        for j in debits:
            derr=derr+j
            conteor=conteor+1
        promedio=derr/conteor
        print("Promedio de debitos",promedio)
    if i == 7:
        conteor=0
        derr=0
        for j in credits:
            derr=derr+j
            conteor=conteor+1
        promedio=derr/conteor
        print("Promedio de creditos",promedio)
    if i == 8:
        derr=0
        for j in debits:
            if j > derr:
                derr=j
        print("Debito mayor:",derr)
    if i == 9:
        print("Conteo de debitos:",conteod)
        print("conteo de creditos:",conteoc)
    if i == 10:
        for j in debits:
            print("Debitos:",j)
        for j in credits:
            print("Creditos:",j)
    if i == 11:
        credits.clear()
        print("Los creditos se han borrado exitosamente")
        