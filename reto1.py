#Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.
#Instrucciones:
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.

print("En este programa quiero saber que preferencias tienes para que juntos creemos tu contraseña ideal especificando la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.")

#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
ancho_clave = int(input("Ingresa cuantos caracteres quieres que tenga tu contraseña."))
opcion_usuario = int(input("Digita 1 si quieres incluir letras minusculas,letras mayusculas, caracteres alfanumericos y simbolos.  Digite 2 si quieres solo incluir letras minusculas,letras mayusculas y caracteres alfanumericos. Digita 3 si quieres solo incluir letras minusculas y letras mayusculas. Y digita 4 si quieres que tu contraseña solo sea de letras minusculas"))
#Utilizará una función para generar la contraseña según las preferencias del usuario.
def con_gen_usuario ():
  print(f"Recuerda que tu contraseña solo va a ser de {ancho_clave} caracteres como maximo y sabiendo eso:")
if opcion_usuario == 1 : 
    l_min_in = input("Ingresa las letras minusculas que quieres en tu contraseña.")
    l_mayus_in = input("Ingresa las letras mayusculas quieres que tenga tu contraseña.")
    n_nums_in = input("Ingresa los numeros quieres que tenga tu contraseña.")
    n_sim_in = input("Ingresa los simbolos quieres que tenga tu contraseña.")
    
    c_l_min = len(l_min_in)
    c_l_mayu = len(l_mayus_in)
    c_num = len(n_nums_in)
    c_sim = len(n_sim_in)
    contraseña_generada = c_num + c_sim + c_l_min + c_l_mayu
    #Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.

    if contraseña_generada > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
    else: print(f"La contraseña es: {l_mayus_in+l_min_in+n_nums_in+n_sim_in}")

elif opcion_usuario == 2 : 
    l_min_in2 = input("Ingresa las letras minusculas que quieres en tu contraseña.")
    l_mayus_in2 = input("Ingresa las letras mayusculas quieres que tenga tu contraseña.")
    n_nums_in2 = input("Ingresa los numeros quieres que tenga tu contraseña.")
    
    c_l_min2 = len(l_min_in2)
    c_l_mayu2 = len(l_mayus_in2)
    c_num2 = len(n_nums_in2)
    
    contraseña_generada2 = c_num2+ c_l_min2 + c_l_mayu2

    if contraseña_generada2 > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
    else: print(f"La contraseña es: {l_mayus_in2+l_min_in2+n_nums_in2}")
elif opcion_usuario == 3 : 
    l_min_in3 = input("Ingresa las letras minusculas que quieres en tu contraseña.")
    l_mayus_in3 = input("Ingresa las letras mayusculas quieres que tenga tu contraseña.")
    
    c_l_min3 = len(l_min_in3)
    c_l_mayu3 = len(l_mayus_in3)

    contraseña_generada3 = c_l_min3 + c_l_mayu3

    if contraseña_generada3 > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
    else: print(f"La contraseña es: {l_mayus_in3+l_min_in3}")

if opcion_usuario == 4 : 
    l_min_in4 = input("Ingresa las letras minusculas que quieres en tu contraseña.")
    
    c_l_min4 = len(l_min_in)

    contraseña_generada4 = c_l_min

    if contraseña_generada4 > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
    else: print(f"La contraseña es: {l_min_in4}")
else : print("La opcion ingresada no esta en las opciones anteriores.")
#Si el usuario decide salir, se despedirá y el programa se cerrará.
opcion2 = input("Deseas salir: S para si y N para no")
if opcion2 == "S" : print("Hasta luego, me diverti mucho contigo")
else : print("Por ahora me despido mientras mejoran mi programa para darte mas opciones.")

