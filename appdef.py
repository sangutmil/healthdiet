import os
import openai
import gradio as gr


#enlazar tu programa de Python con tu archivo HTML
from flask import Flask, render_template

appdef = Flask("appdef")

# Ruta para manejar la solicitud de redireccionamiento desde la imagen
@appdef.route('/http://127.0.0.1:7860')
def redirigir():
    # Agrega aquí el código para procesar la solicitud de redireccionamiento
    return "Hola desde la página de redirección"

# Rutas y lógica adicional de tu aplicación
# ...

if appdef == 'http://127.0.0.1:7860':
    appdef.run()
    
    


#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Detallanos sobre tu edad, sexo, altura, alérgenos, actividad física y tipo de cambio físico que quieras hacer: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Estás ante el chat de Pérdida de Peso</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("ENVIAR")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)


# Importa la biblioteca Flask para crear aplicaciones web en Python
from flask import Flask, request, render_template, redirect

# Crea una instancia de la aplicación Flask
appdef = Flask(appdef)

# Crea una variable global para el número máximo de preguntas gratuitas
MAX_PREGUNTAS_GRATUITAS = 3

# Inicializa el contador de preguntas realizadas a cero
preguntas_realizadas = 0

# Define una función para obtener la respuesta del modelo de lenguaje
def obtener_respuesta(pregunta):
    # Código para obtener la respuesta del modelo de lenguaje GPT-3
    respuesta = "Respuesta a la pregunta: " + pregunta
    return respuesta

# Define una función que maneje la ruta de la página de chat
@appdef.route('http://127.0.0.1:7860', methods=['GET', 'POST'])
def chat():
    global preguntas_realizadas  # Usa la variable global preguntas_realizadas

    # Verifica si el usuario ha enviado una pregunta
    if request.method == 'POST':
        pregunta = request.form['pregunta']
        respuesta = obtener_respuesta(pregunta)

        # Incrementa el contador de preguntas realizadas
        preguntas_realizadas += 1

        # Verifica si el usuario ha excedido el límite de preguntas gratuitas
        if preguntas_realizadas > MAX_PREGUNTAS_GRATUITAS:
            # Redirige al usuario a la página de pago
            return redirect('http://127.0.0.1:5500/pasarela/index.html')

        # Renderiza la plantilla de la página de chat con la respuesta
        return render_template('http://127.0.0.1:7863', pregunta=pregunta, respuesta=respuesta)

    # Renderiza la plantilla de la página de chat vacía
    return render_template('http://127.0.0.1:7860')

# Define una función que maneje la ruta de la página de pago
@appdef.route('http://127.0.0.1:5500/pasarela/index.html')
def pagodechat():
    # Renderiza la plantilla de la página de pago
    return render_template('http://127.0.0.1:5500/pasarela/index.html')

# Ejecuta la aplicación Flask en modo de depuración
if appdef == 'inicio':
    appdef.run(debug=True)
