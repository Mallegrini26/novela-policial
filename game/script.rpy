# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

# Definición de personajes

define d = Character("Detective", color="#FF0000")
define s_1 = Character("Suspect 1", color="#00FF00")
define s_2 = Character("Suspect 2", color="#0000FF")
define n = Character("Narrador")
define m = Character("Mayordomo", color="#800080")
define t = Character("Testigo", color="#FFA500")

# Definición de imágenes (ajusta las rutas según tus archivos)
image bg office = "images/bg_office.jpg"                 # Escena inicial
image bg mansion = "images/bg_mansion.jpg"               # Escena mansión
image bg library = "images/bg_library.jpg"               # Escena biblioteca
image bg hallway = "images/bg_hallway.jpg"               # Escena pasillo
image bg kitchen = "images/bg_kitchen.jpg"               # Escena cocina
image bg mansion_hallway = "images/bg_mansion_hallway.jpg" # Escena pasillo mansión
image bg mansion_study = "images/bg_mansion_study.jpg"   # Escena estudio
image bg police_station = "images/bg_police_station.jpg" # Escena estación de policía
image bg mansion_exterior = "images/bg_mansion_exterior.jpg" # Escena exterior mansión
image bg crime_scene = "images/bg_crime_scene.jpg"       # Escena lugar del crimen
image bg servants_room = "images/bg_servants_room.jpg"   # Escena habitación del mayordomo
image bg secret_diary = "images/bg_secret_diary.jpg"     # Escena diario secreto
image bg hidden_witness = "images/bg_hidden_witness.jpg" # Escena testigo oculto
image bg garden = "images/bg_garden.jpg"                 # Escena jardín
image bg love_letter = "images/bg_love_letter.jpg"       # Escena carta de amor
image bg basement = "images/bg_basement.jpg"             # Escena sótano
image bg hidden_weapon = "images/bg_hidden_weapon.jpg"   # Escena arma oculta
image bg final_revelation = "images/bg_final_revelation.jpg" # Escena final

# El juego comienza aquí.

label start:
    $ pista = False
    $ cantidad_sospechoso = 0
    $ nombre = "Cruso"
    
    scene bg_office
    n "Una  carta llega a la oficina del detective [nombre]. Un asesinato ha ocurrido en la mansión Blackwood."
    d "Parece que esta vez tenemos un caso complicado. Hay dos sospechosos principales."
    jump escena_mansion

label escena_mansion:
    scene bg_mansion
    d "Debo interrogar a los sospechosos y juntar pistas."

    jump mapa
    menu:
        "Interrogar a Suspect 1":
            jump interrogatorio_suspect1
        "Interrogar a Suspect 2":
            jump interrogatorio_suspect2
label interrogatorio_suspect1:
    scene bg_library
    s_1 "Yo no fui. Estaba en la biblioteca cuando ocurrió el asesinato."
    jump decidir

label interrogatorio_suspect2:
    scene bg_hallway
    s_2 "No sé nada. Solo escuché un ruido en el pasillo."
    jump decidir

label decidir:
    scene bg_office
    d "Debo tomar una decisión. ¿Quién es el asesino?"
    menu:
        "Acusar a Suspect 1":
            jump final_suspect1
        "Acusar a Suspect 2":
            jump final_suspect2
        "Seguir investigando":
            jump investigacion_adicional

label investigacion_adicional:
    scene bg_kitchen
    n "El detective [nombre] encuentra una pista crucial: un guante con sangre en la cocina."
    d "Esto cambia todo."
    jump escena_sospecha

label escena_sospecha:
    scene bg_mansion_hallway
    n "El detective [nombre] observa huellas de barro en el pasillo que llevan al estudio."
    d "Esto no concuerda con los testimonios."
    jump escena_descubrimiento

label escena_descubrimiento:
    scene bg_mansion_study
    n "El detective [nombre] descubre un papel quemado en la chimenea con el nombre de la víctima."
    d "Parece que alguien intentó ocultar pruebas."
    menu:
        "Acusar a Suspect 1":
            jump final_suspect1
        "Acusar a Suspect 2":
            jump final_suspect2
        "Revelar la verdad":
            jump final_verdad

# Escenas adicionales integradas
label escena_1:
    scene bg_mansion_exterior
    n "El detective [nombre] llega a la mansión Blackwood. El lugar parece sombrío y lleno de secretos."
    d "Aquí es donde todo comenzó. Debo estar alerta."
    jump escena_2

label escena_2:
    scene bg_crime_scene
    n "El detective [nombre] inspecciona el lugar del crimen. Hay sangre en el suelo y signos de lucha."
    d "Algo no cuadra aquí. ¿Por qué no hay más desorden?"
    jump escena_3

label escena_3:
    scene bg_servants_room
    n "El detective [nombre] habla con el mayordomo, quien parece nervioso."
    m "Yo no vi nada, señor. Estaba ocupado en mis tareas."
    d "¿Por qué tiemblas? ¿Qué estás ocultando?"
    jump escena_4

label escena_4:
    scene bg_secret_diary
    n "El detective [nombre] encuentra un diario escondido en la habitación de la víctima."
    d "Este diario podría contener la clave del caso."
    jump escena_5

label escena_5:
    scene bg_hidden_witness
    narrator "Un testigo oculto se acerca al detective en secreto."
    t "Vi algo esa noche. Alguien más estaba aquí."
    d "¿Quién era? ¡Dime!"
    jump escena_6

label escena_6:
    scene bg_garden
    n "El detective [nombre] investiga el jardín y encuentra huellas extrañas."
    d "Estas huellas no coinciden con las de los sospechosos."
    jump escena_7

label escena_7:
    scene bg_love_letter
    n "El detective [nombre] descubre una carta de amor entre la víctima y alguien más."
    d "¿Había una relación secreta? Esto cambia todo."
    jump escena_8

label escena_8:
    scene bg_basement
    n "El detective [nombre] baja al sótano y encuentra una puerta cerrada con llave."
    d "¿Qué hay aquí que no quieren que vea?"
    jump escena_9

label escena_9:
    scene bg_hidden_weapon
    n "El detective [nombre] encuentra un arma escondida en el sótano."
    d "Esta es el arma del crimen. Pero, ¿quién la escondió aquí?"
    jump escena_10

label escena_10:
    scene bg_final_revelation
    n "El detective [nombre] reúne todas las pistas y confronta al verdadero culpable."
    d "¡Mayordomo! Tú eres el asesino. Confiesa."
    m "¡No puedo creer que me hayas descubierto!"
    return

# Finales existentes
label final_suspect1:
    scene bg_police_station
    n "El detective [nombre] acusa a Suspect 1, quien es arrestado. Pero... ¿era realmente el culpable?"
    return

label final_suspect2:
    scene bg_police_station
    n "El detective [nombre] acusa a Suspect 2, quien confiesa el crimen y es encarcelado."
    return

label final_verdad:
    scene bg_mansion_study
    n "El detective [nombre] revela que ninguno de los sospechosos era culpable. El verdadero asesino era el mayordomo."
    return


