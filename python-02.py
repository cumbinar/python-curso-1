usuario = input("Ingresa tu nombre  ")
agua = int(input(" Ingrese el valor del agua  "))
luz = int(input(" Ingrese el valor de la luz  "))
gas = int(input(" Ingrese el valor del Gas  "))
web = int(input(" Ingrese el valor de la web  "))

servicios = agua + luz + gas + web

descuento = servicios * 0.10

valor_a_pagar = servicios - descuento


print(usuario+"  el valor a pagar es  " + str(valor_a_pagar))

input()
