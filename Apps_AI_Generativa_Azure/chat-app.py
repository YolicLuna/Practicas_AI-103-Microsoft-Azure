"""
Antes de comenzar, recuerda que debes tenes implementado un proyecto en Foundry,
en caso de que aun no lo tengas ouedes consutar Despliegue_de_Modelo_en_Foundry.md, 
que es donde se indica como realizar ese proceso.

En esta practica estaremos trabajando con un modelo gpt-5.2.

Se requerira el uso de endpoint para conectar al modelo desde la aplicacion cliente,
En esta practca utilizaremos el SDK de OpenAI para comunicarnos con el modelo y el endpoint
de Azure OpenAI con autenticación de ID de Entra para conectarnos a él.

El endpoint lo podrás encontras en la pagina de inicio despues de crear tu proyecto
y de implementar el modelo de AI.

Se recomienda crear un entorno de desarrollo .env e instalar las dependencias indicadas
en el archivo requirements.txt usando 'pip install -r requirements.txt'.

"""

# Primero se importan las librerias necesarias para el funcionamiento del script.
import os
from dotenv import load_dotenv
from openai import OpenAI # Esta libreria es la que nos permite conectarnos al modelo de AI.
from azure.identity import DefaultAzureCredential, get_bearer_token_provider # Esta libreria es la que nos permite conectarnos al endpoint de Azure OpenIA.


# Se define la funcion principal del script, que es asincrona para poder manejar las respuestas del modelo de AI de manera eficiente.
def main(): 
    # Se limpia la consola para que el usuario pueda ver mejor la salida del script.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Se utiliza un bloque try-except para manejar posibles errores durante la ejecucion del script.
    try:
        # Se cargan las variables de entorno desde el archivo .env para obtener la configuracion necesaria.
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Se inicializa el cliente asincrono de OpenAI con la configuracion obtenida.
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(), "https://ai.azure.com/.default"
        )

        # Se crea una instancia del cliente asincrono de OpenAI para poder enviar solicitudes al modelo de AI. 
        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=token_provider
        )
        
        # Se inicializa una variable para almacenar el ID de la ultima respuesta del modelo de AI, lo que permite mantener el contexto de la conversacion.
        last_response_id = None

        # Se inicia un bucle infinito para permitir al usuario ingresar prompts de manera continua hasta que decida salir usando la palabra clave "quit".
        while True:
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # Se envia el prompt ingresado por el usuario al modelo de AI y se obtiene la respuesta correspondiente.

            """
            En los siguientes bloques de codigo se muestran diferentes formas de enviar el prompt al modelo de AI y obtener la respuesta.
            Se recomienda utilizar la ultima forma, que es la que permite mantener el contexto de la conversacion y obtener respuestas mas coherentes y precisas.
            En caso de querer utilizar alguna de las otras formas, se debe comentar la ultima forma y descomentar la que se desea utilizar.

            La primera forma utiliza el metodo chat.completions.create() para enviar el prompt y obtener la respuesta, pero no permite mantener el contexto de la conversacion.
            La segunda forma utiliza el metodo responses.create() para enviar el prompt y obtener la respuesta, pero no permite mantener el contexto de la conversacion.
            La tercera forma utiliza el metodo responses.create() para enviar el prompt y obtener la respuesta, y permite mantener el contexto de la conversacion utilizando el parametro previous_response_id.
            La cuarta forma utiliza el metodo responses.create() para enviar el prompt y obtener la respuesta, y permite mantener el contexto de la conversacion utilizando el parametro previous_response_id, ademas de permitir obtener la respuesta de manera asincrona utilizando el parametro stream=True.
            """

            # completion = openai_client.chat.completions.create(
            #     model=model_deployment,
            #     messages=[
            #         {
            #             "role": "system",
            #             "content": "You are a helpful AI assistant that answers questions and provides information."
            #         },
            #         {
            #             "role": "user",
            #             "content": input_text
            #         }
            #     ]
            # )
            # print(completion.choices[0].message.content)



            # response = openai_client.responses.create(
            #             model=model_deployment,
            #             instructions="You are a helpful AI assistant that answers questions and provides information.",
            #             input=input_text
            # )
            # print(response.output_text)



            # response = openai_client.responses.create(
            #             model=model_deployment,
            #             instructions="You are a helpful AI assistant that answers questions and provides information.",
            #             input=input_text,
            #             previous_response_id=last_response_id,
            # )
            # print(response.output_text)
            # last_response_id = response.id


            stream = openai_client.responses.create(
                        model=model_deployment,
                        instructions="You are a helpful AI assistant that answers questions and provides information.",
                        input=input_text,
                        previous_response_id=last_response_id,
                        stream=True
            )
            for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="")
                elif event.type == "response.completed":
                    last_response_id = event.response.id
            print()

    # Se maneja cualquier excepcion que pueda ocurrir durante la ejecucion del script, 
    # imprimiendo el error en la consola para que el usuario pueda identificarlo y solucionarlo.
    except Exception as ex:
        print(ex)

# Se verifica si el script se esta ejecutando como programa principal y se llama a la funcion main() para iniciar la ejecucion del script.
if __name__ == '__main__': 
    main() 