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
import asyncio
from openai import AsyncOpenAI # Esta libreria es la que nos permite conectarnos al modelo de AI.
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider # Esta libreria es la que nos permite conectarnos al endpoint de Azure OpenIA.


# Se define la funcion principal del script, que es asincrona para poder manejar las respuestas del modelo de AI de manera eficiente.
async def main(): 

    # Se limpia la consola para que el usuario pueda ver mejor la salida del script.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Se utiliza un bloque try-except para manejar posibles errores durante la ejecucion del script.
    try:
        # Se cargan las variables de entorno desde el archivo .env para obtener la configuracion necesaria.
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Se inicializa el cliente asincrono de OpenAI con la configuracion obtenida.
        credential = DefaultAzureCredential()
        token_provider = get_bearer_token_provider(
        credential, "https://ai.azure.com/.default"
        )

        # Se crea una instancia del cliente asincrono de OpenAI para poder enviar solicitudes al modelo de AI.
        async_client = AsyncOpenAI(
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
            response = await async_client.responses.create(
                        model=model_deployment,
                        instructions="You are a helpful AI assistant that answers questions and provides information.",
                        input=input_text,
                        previous_response_id=last_response_id
            )

            # Se imprime la respuesta del modelo de AI en la consola para que el usuario pueda verla.
            assistant_text = response.output_text
            print("Assistant:", assistant_text)
            last_response_id = response.id

            
    # Se maneja cualquier excepcion que pueda ocurrir durante la ejecucion del script, 
    # imprimiendo el error en la consola para que el usuario pueda identificarlo y solucionarlo.
    except Exception as ex:
        print(ex)

    finally:
        # Se cierra la conexion con el cliente asincrono de OpenAI y se cierra la credencial para liberar recursos.
        await credential.close()


# Se verifica si el script se esta ejecutando como programa principal y se llama a la funcion main() para iniciar la ejecucion del script.
if __name__ == '__main__': 
    asyncio.run(main())