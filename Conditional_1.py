#input 
Cant_minutos=input("digite la cant_minuto")
Cant_minutos=int(Cant_minutos)

#procesing 
if Cant_minutos<=3:
    valor_llamada=300
else:
    valor_llamada=300+50*(Cant_minutos-3)
#output
print("el valor de la llamada es:" + str(valor_llamada))
