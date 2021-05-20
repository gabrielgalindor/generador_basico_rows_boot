import math
import time

#txt = "welcome to the jungle"
#x = txt.split()
#print(x)

#funcion para opcion 1
def generarst(idname="fila",numid=1,listaclass=[None],colcant=1):

    masterdiv = "	<div "
    idrows = str(numid)
    masterdiv = masterdiv+" id='"+idname+idrows+"' "
    contador2 = len(listaclass)
    k1 = 0
    if listaclass[k1] != None:
        masterdiv = masterdiv+"class='row "
        while k1 < contador2:
            if listaclass[k1] != None:
                masterdiv=masterdiv+" "+listaclass[k1]
            k1+=1
        masterdiv = masterdiv+"' "
    masterdiv=masterdiv+">"

    
    
    # check de cantidad de columnas menor a 12
    if colcant>12:
        colcant = 12
    numcols = math.floor(12/colcant)
    k2=1
    while k2<=colcant:
        strincol = "col-"+str(numcols)
        masterdiv = masterdiv+"\n	    <div class='"+strincol+"'> \n            	escriba--aca  \n	     </div>"
        k2+=1
    masterdiv = masterdiv+"\n	</div>"
    return masterdiv
    
    
        

        



def fopcion1():

    container_type = input("\n Ingrese f para fluid o n para normal \n  gogaxgen: ")
    if container_type=="f":
        print("Debugg  opcion fluid")
    elif container_type=="n":
        print("Debugg  opcion normal")
    else:
        print("gogagen - Error: Opcion NO valida de container, revise nuevamente el input")
        return
    row_n = input("\n Ingrese la CANTIDAD # de filas (rows) \n  gogaxgen: ")
    row_n = int(row_n)
    IDmaster = input("\n Ingrese id (STRING) de la fila (rows) \n  gogaxgen: ")
    col_n = input("Ingrese la CANTIDAD # de columnas (cols) - recuerde que no existen valores mayores a 12 \n  gogaxgen: ")
    col_n = int(row_n)

    class_name = input("Ingrese un clases (con espacios por clase) \n  gogaxgen: ")
    class_name = class_name.split()
    
    print(IDmaster)
    cont1 = 0

    if container_type=="f":
        print("<div class='container-fluid'> \n")
    elif container_type=="n":
        print("<div class='container'> \n")

    while cont1 < row_n:
        finalrow = generarst(idname=IDmaster,numid=1,listaclass=class_name,colcant=col_n)
        print(finalrow)
        cont1 +=1
    print("</div>")
    return



    







print("Bienvenido al generador de html por Gabriel Galindo \n")
print("Version: 0.0.1 - Fecha Publicacion: 12/Sep/2020 \n")
time.sleep(0.2)

opcion_1 = input("Ingrese según la opción: \n 1- Para generar rows con el mismo formato \n 2- Para generar rows con formato independiente \n gogaxgen: ")
print("\n Valor ingresado {0}".format(opcion_1))

opcion_1 = int(opcion_1)

if opcion_1==1:
    fopcion1()
elif opcion_1==2:
    print("No disponible aun")
else:
    print("No se reconoce el valor del menu - opcion 1 \n intentelo nuevamente")


#Inicio de seleccion 



