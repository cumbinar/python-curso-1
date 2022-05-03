'''Hacer un programa que permita leer una fecha solicitando el número de día, el número de
mes y el año (ej: primero 20, luego 9, y luego 2013). Verifique que es correcta, el día
existe y febrero tiene 29 días para los años bisiestos (cada 4 años) y la escriba en el formato
dd/mmm/aaaa, donde dd es el número del día, mmm es la abreviatura en 3 letras del mes
(ene, feb, mar…), y aaaa el año. (ej: 20/sep/2013)'''

dia = int(input("ingrese el dia:  "))
mes = int(input("Ingrese el número del mes: "))
anio = int(input("Ingrese el número del año: "))

if(anio%4 == 0):
    es_bisiesto = True  #variable bandera
elif(anio%100 == 0):
    es_bisiesto = False
elif(anio%4 ==0):
    es_bisiesto = True
else:
    es_bisiesto = False

if(mes == 2):
    if(es_bisiesto):
        if(dia>0 and dia<=29):
            es_correcta = True
        else: 
            es_correcta = False
    else:
        if(dia>0 and dia<=28):
            es_correcta = True
        else: 
            es_correcta = False
else:
    if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):  
        if(dia>0 and dia<=31):
            es_correcta = True
        else: es_correcta = False
    else:
        if(mes==4 or mes==6 or mes==9 or mes==11):
            if(dia>0 and dia<=30):
                es_correcta = True 
            else: 
                es_correcta = False  
        else: 
            es_correcta = False  

if (es_correcta):
    match mes:
        case 1:
            messtr = "ene"   
        case 2:
            messtr = "feb"
        case 3:
            messtr = "mar"
        case 4:
            messtr = "abr"
        case 5:
            messtr = "may"
        case 6:
            messtr = "jun"
        case 7:
            messtr = "jul"
        case 8:
            messtr = "ago"
        case 9:
            messtr = "sep"
        case 10:
            messtr = "oct"
        case 11:
            messtr = "nov"
        case 12:
            messtr = "dic"
    print(str(dia)+ "/"+ messtr + "/"+ str(anio))
else:
    print("Fecha incorrecta")

if es_bisiesto:
    print("El año "+ str(anio)+ " ES BISIESTO" )
else:
    print("El año " + str(anio) + " No es bisiesto")
