# Para manipular JSON.
import json
# Para acceder a una url.
import requests
# Para generar un número aleatorio
import random
# Para poder tener ventana.

#Funciones
def respuestaValida(self,numero):
    r_incorrecta=True
    while r_incorrecta:
        try:
            respuesta=int(self.spinBoxNumRespuesta.value())
            if 1<=respuesta<=numero:
                r_incorrecta=False
                return respuesta
            else:
                print("Invalid answer. Please choose a number between 1 and", numero)
        except ValueError:
            print("Sorry, you should write a valid answer: ")
def validarNumPreguntas():
    r_incorrecta=True
    while r_incorrecta:
        try:
            respuesta=int(input("How many questions do yo want to answer?\n(from 1 to 50):"))
            if 1<=respuesta<=50:
                r_incorrecta=False
                return respuesta
            else:
                print("Invalid answer. Please choose a number between 1 and 50.")
        except ValueError:
            print("Sorry, you should enter a number between 1 and 50. ")

# Interacción con el usuario
def saludaUsuario():   
    numPreguntas=validarNumPreguntas()
    return numPreguntas

# Hacemos la solicitud de los datos a la url.
def generaCategoria():
    categoria=int(random.randint(9,30))
    return categoria

def llamadaApi(numPreguntas,categoria):
    API_url=f"https://opentdb.com/api.php?amount={numPreguntas}+&category={categoria}"
    respuesta=requests.get(API_url)
# Convertimos el resultado de llamada a la API "JSON" a una estructura de datos manejable
    datos=json.loads(respuesta.text)
# La URL podría devolvernos un JSON, de momento lo voy a controlar con un while.
    while datos["response_code"] == 1:
        categoria = int(random.randint(9, 30))
        API_url = f"https://opentdb.com/api.php?amount={numPreguntas}&category={categoria}"
        respuesta = requests.get(API_url)
        datos = json.loads(respuesta.text)
        print(type(datos))
    return datos

"""def generaCuestionario(datos,numPreguntas):
    preguntas=datos["results"]
    cadenaTotal=""
    cadenaCategoria="The category is "+preguntas[0]["category"]+"\n"
    
    for pregunta in preguntas:
        opciones=[]
        cadenaPregunta=pregunta["question"]
        # Este for añade las respuestas malas a una lista de opciones
        for numRespuesta in range(len(pregunta["incorrect_answers"])): 
            opciones.append(pregunta["incorrect_answers"][numRespuesta])
        # Añadimos la respuesta correcta
        opciones.append(pregunta["correct_answer"])
        random.shuffle(opciones)
        cadenaOpciones=""
        contador=0
        for respuesta in range(len(opciones)):
            contador=contador+1
            cadenaOpciones+=f"{contador} {opciones[respuesta]}\n"

    cadenaTotal=cadenaCategoria+cadenaPregunta+cadenaOpciones        
    return cadenaTotal,opciones"""

# recogemos la respuesta del usuario y realizo la comprobación
# prevengo que la respuesta no sea un carácter o un número mayor que las opciones disponibles.

def respuestaUsuario(self, opciones, pregunta):
    respuestaUsuario=-1
    print(opciones)
    respuestaUsuario=respuestaValida(self,len(opciones))
    respuestaUsuario-=1
    if opciones[respuestaUsuario]==pregunta["correct_answer"]:
        self.aciertos+=1
    else:
        self.fallos+=1


def calculaResultado(aciertos,fallos,numPreguntas):    
    cadenaResultado=""
    porcentaje_Acierto = (aciertos/numPreguntas) * 100
    if porcentaje_Acierto>=50:
        cadenaResultado+="Well done! You have passed the quiz!\n"
    else:
        cadenaResultado+="You lose... Don't worry, you'll get them next time!\n"

    cadenaResultado+=(f"You had {aciertos} correct answers.\n")
    cadenaResultado+=(f"You had {fallos} incorrect answers.\n")
    cadenaResultado+=(f"Your final score is {porcentaje_Acierto}\n")
    return cadenaResultado