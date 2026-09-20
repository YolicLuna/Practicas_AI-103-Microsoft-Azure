# Aplicaciones de IA Generativa con Azure

Repositorio de prácticas enfocado en la creación de aplicaciones cliente para interactuar con modelos de Azure OpenAI desde Python. Esta carpeta está orientada a explorar cómo se conecta una aplicación con un modelo desplegado en Microsoft Foundry y cómo se gestiona la autenticación, el contexto de conversación y la interacción con el modelo mediante el SDK de OpenAI.

---

## Prácticas

### [Chat con Azure OpenAI](./chat-app.py)
Aplicación de consola que permite enviar prompts al modelo desplegado y recibir respuestas en tiempo real.
* Conexión con el endpoint de Azure OpenAI.
* Autenticación mediante `DefaultAzureCredential` y `get_bearer_token_provider`.
* Uso del SDK de OpenAI para enviar solicitudes al modelo.
* Mantenimiento del contexto de la conversación con `previous_response_id`.
* Soporte para respuestas en streaming con salida incremental.

**Enfoque:** conexión con IA + autenticación + contexto + interacción conversacional

---

### [Chat asíncrono con Azure OpenAI](./chat-async.py)
Versión de la práctica anterior implementada con programación asíncrona usando `asyncio`.
* Uso de `AsyncOpenAI` para manejar llamadas no bloqueantes.
* Integración con Azure Identity de manera segura.
* Bucle de conversación continua hasta que el usuario escribe `quit`.
* Manejo de errores y cierre de credenciales al finalizar la ejecución.
* Estructura optimizada para aplicaciones que requieren respuestas concurrentes o más eficientes.

**Enfoque:** programación asíncrona + integración con modelos + experiencia de chat fluida

---

### [Dependencias del proyecto](./requirements.txt)
Archivo con las librerías necesarias para ejecutar las prácticas de esta carpeta.
* `python-dotenv` para cargar variables del entorno.
* `azure-identity` para autenticación con Azure.
* `openai` para consumir el SDK del modelo.
* `aiohttp` para soporte adicional de conexiones asíncronas.

**Enfoque:** preparación del entorno + configuración del proyecto

---

## Enfoque de la carpeta
Los ejercicios de esta sección están orientados a:
* Conectar aplicaciones Python con modelos de IA desplegados en Azure.
* Explorar la forma de autenticarse de manera segura con Microsoft Entra ID.
* Entender cómo mantener contexto en conversaciones con modelos generativos.
* Comparar una implementación síncrona y otra asíncrona.
* Aprender los fundamentos para integrar IA generativa en aplicaciones reales.

---

## Tecnologías utilizadas
* Python.
* Azure OpenAI.
* OpenAI SDK.
* Azure Identity.
* Python-dotenv.
* Asyncio.
* Microsoft Foundry.

---

## Nota
Cada práctica incluye una lógica de conexión con el modelo que requiere:
* Tener un proyecto y un modelo desplegado en Foundry.
* Definir las variables de entorno en un archivo `.env` con los valores de `AZURE_OPENAI_ENDPOINT` y `MODEL_DEPLOYMENT`.
* Instalar las dependencias mediante `pip install -r requirements.txt`.

---

## Objetivo
Desarrollar habilidades prácticas para crear aplicaciones generativas con Azure, comprender el flujo de autenticación con servicios de IA y construir experiencias conversacionales conectadas a modelos reales desplegados en Microsoft Foundry.
