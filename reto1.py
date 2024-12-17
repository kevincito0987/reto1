#Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.
#Instrucciones:
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
import re
print("En este programa quiero saber que preferencias tienes para que juntos creemos tu contraseña ideal especificando la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.")

#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
ancho_clave = int(input("Ingresa cuantos caracteres quieres que tenga tu contraseña."))
opcion_usuario = int(input("Digita 1 si quieres incluir letras minusculas,letras mayusculas, caracteres alfanumericos y simbolos.  Digite 2 si quieres solo incluir letras minusculas,letras mayusculas y caracteres alfanumericos. Digita 3 si quieres solo incluir letras minusculas y letras mayusculas. Y digita 4 si quieres que tu contraseña solo sea de letras minusculas"))
#Utilizará una función para generar la contraseña según las preferencias del usuario.
def gen_le_min_con():
  while True:
    l_min = input("Ingrese una cadena de letras minúsculas: ")

    # Verificar si todos los caracteres son letras minúsculas
    if l_min.isalpha() and l_min.islower():
        print("¡Entrada válida!")
        break  # Salir del bucle si la entrada es correcta
    else:
        print("Error: La entrada debe contener solo letras minúsculas.")
  return l_min
def gen_le_may_con():
  while True:
    l_may = input("Ingrese una cadena de letras minúsculas: ")

    # Verificar si todos los caracteres son letras minúsculas
    if l_may.isalpha() and l_may.islower():
        print("¡Entrada válida!")
        break  # Salir del bucle si la entrada es correcta
    else:
        print("Error: La entrada debe contener solo letras minúsculas.")
  return l_may
def gen_num_con():
  while True:
     num_in = input("Ingrese solo números: ")
    # Verificar si todos los caracteres son números
     if num_in.isdigit():
        print("¡Entrada válida!")
        break  # Salir del bucle si la entrada es correcta
     else:
        print("Error: La entrada debe contener solo números.")
  return num_in
def car_esp_in():
    patron = r'^[^a-zA-Z0-9\s]+$'

    while True:
        car_in = input("Ingrese solo caracteres especiales: ")
        if re.match(patron, car_in):
            print("Entrada válida.")
            return car_in
        else:
            print("Error: La entrada debe contener solo caracteres especiales.")
            
def solicitar_entrada_con_limite(prompt, limite):
    while True:
        entrada = input(prompt)
        if len(entrada) <= limite:
            return entrada
        else:
            print(f"Has excedido el límite de {limite} caracteres. Intenta nuevamente.")
            
def uni_car_con_gen1():
    l_min_in = gen_le_min_con()
    l_mayus_in = gen_le_may_con()
    n_nums_in = gen_num_con()
    n_sim_in = car_esp_in()
    c_l_min = len(l_min_in)
    c_l_mayu = len(l_mayus_in)
    c_num = len(n_nums_in)
    c_sim = len(n_sim_in)
    contraseña_generada = c_num + c_sim + c_l_min + c_l_mayu
    return contraseña_generada

def uni_car_con_gen2():
    l_min_in2 = gen_le_min_con()
    l_mayus_in2 = gen_le_may_con()
    n_nums_in2 = gen_num_con()
    
    c_l_min2 = len(l_min_in2)
    c_l_mayu2 = len(l_mayus_in2)
    c_num2 = len(n_nums_in2)
    
    contraseña_generada2 = c_num2+ c_l_min2 + c_l_mayu2
    return contraseña_generada2
  
def uni_car_con_gen3():
    l_min_in3 = gen_le_min_con()
    l_mayus_in3 = gen_le_may_con()
    
    c_l_min3 = len(l_min_in3)
    c_l_mayu3 = len(l_mayus_in3)

    contraseña_generada3 = c_l_min3 + c_l_mayu3
    return contraseña_generada3
  
def uni_car_con_gen4():
    l_min_in4 = gen_le_min_con()

    contraseña_generada4 = l_min_in4
    return contraseña_generada4
  
def con_gen_usuario ():
   print(f"Recuerda que tu contraseña solo va a ser de {ancho_clave} caracteres como maximo y sabiendo eso:")
   if opcion_usuario == 1 : 
     contraseña_generada_to = uni_car_con_gen1()
    #Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
     contraseña_eval = solicitar_entrada_con_limite(contraseña_generada_to)
     if contraseña_eval == True : print(contraseña_generada_to)
   elif opcion_usuario == 2 : 
     contraseña_generada2_to = uni_car_con_gen2()

     if contraseña_generada2_to > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
     else: print(f"La contraseña es: {l_mayus_in2+l_min_in2+n_nums_in2}")
   elif opcion_usuario == 3 : 
     contraseña_generada3_to = uni_car_con_gen3()

     if contraseña_generada3_to > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
     else: print(f"La contraseña es: {l_mayus_in3+l_min_in3}")

   if opcion_usuario == 4 : 
     contraseña_generada4_to = uni_car_con_gen4()

     if contraseña_generada4_to > ancho_clave : print(f"Ingresa un numero menor a : {ancho_clave}.")
     else: print(f"La contraseña es: {l_min_in4}")
   else : print("La opcion ingresada no esta en las opciones anteriores.")
#Si el usuario decide salir, se despedirá y el programa se cerrará.
opcion2 = input("Deseas salir: S para si y N para no")
if opcion2 == "S" : print("Hasta luego, me diverti mucho contigo")
else : print("Por ahora me despido mientras mejoran mi programa para darte mas opciones.")