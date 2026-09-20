![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-AI%20Foundry-0078D4.svg)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-00A4EF.svg)
![Python](https://img.shields.io/badge/Python-Programming-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-SDK-412991.svg)
![VS Code](https://img.shields.io/badge/VS%20Code-Foundry%20Toolkit-007ACC.svg)

# Prácticas de IA Generativa con Azure

Repositorio de ejercicios y proyectos enfocados en el aprendizaje de inteligencia artificial generativa en Microsoft Azure, con especial atención a Microsoft Foundry, Azure OpenAI y la integración de modelos con aplicaciones cliente desarrolladas en Python.

---

## Propósito

Consolidar conocimientos mediante la creación de prácticas reales relacionadas con:
* Configuración y despliegue de proyectos en Microsoft Foundry.
* Exploración y comparación de modelos de IA.
* Conexión de aplicaciones Python con modelos generativos.
* Autenticación segura con Azure Identity.
* Implementación de chatbots y asistentes conversacionales con contexto.
* Evaluación de modelos con prompts y conjuntos de datos sintéticos.

---

## Estructura del repositorio

Cada archivo y carpeta representa una parte del proceso de aprendizaje en IA generativa con Azure. La estructura del repositorio permite avanzar desde la configuración inicial del proyecto hasta la conexión con modelos y el desarrollo de aplicaciones cliente.

---

## Tecnologías utilizadas

* **Microsoft Foundry / Azure AI Foundry**: creación de proyectos, despliegue de modelos y evaluación.
* **Azure OpenAI**: acceso a modelos generativos mediante endpoints de Azure.
* **Python**: desarrollo de aplicaciones conectadas a IA.
* **OpenAI SDK**: consumo de modelos desde aplicaciones cliente.
* **Azure Identity**: autenticación con Microsoft Entra ID.
* **Python-dotenv**: gestión de variables de entorno.
* **Asyncio**: desarrollo de clientes asíncronos.
* **Visual Studio Code + Foundry Toolkit**: gestión y prueba de proyectos y modelos desde el entorno de desarrollo.

---

## Carpetas y documentos principales

* **[Apps_AI_Generativa_Azure](./Apps_AI_Generativa_Azure)**
  Prácticas centradas en la integración de modelos de IA con aplicaciones Python:
  * [chat-app.py](./Apps_AI_Generativa_Azure/chat-app.py) - Aplicación de chat síncrona con Azure OpenAI.
  * [chat-async.py](./Apps_AI_Generativa_Azure/chat-async.py) - Versión asíncrona para manejar conversaciones de forma más eficiente.
  * [requirements.txt](./Apps_AI_Generativa_Azure/requirements.txt) - Dependencias necesarias para ejecutar las prácticas.
  * [README.md](./Apps_AI_Generativa_Azure/README.md) - Resumen de la carpeta y de cada práctica realizada.

---

* **[Despliegue_de_Modelo_en_Foundry.md](./Despliegue_de_Modelo_en_Foundry.md)**
  Guía paso a paso para crear un proyecto en Microsoft Foundry, implementar un modelo, probarlo y configurar los puntos de conexión necesarios para conectarlo desde aplicaciones cliente.
  * Creación del proyecto en Foundry.
  * Implementación del modelo.
  * Pruebas rápidas con prompts en el portal.
  * Uso de Foundry Toolkit en VS Code.

---

* **[Explora_y_compara_modelos.md](./Explora_y_compara_modelos.md)**
  Documento de análisis de modelos de IA dentro del catálogo de Microsoft Foundry.
  * Exploración del catálogo de modelos.
  * Comparación lado a lado de modelos.
  * Evaluación de rendimiento, calidad y seguridad.
  * Pruebas con prompts comparativos.
  * Generación de evaluaciones con datos sintéticos.

---

* **[Imagenes](./Imagenes)**
  Capturas de pantalla y recursos visuales que acompañan los ejercicios y guías del repositorio.

---

* **[requirements.txt](./requirements.txt)**
  Archivo de dependencias del repositorio principal para ejecutar tareas relacionadas con IA y entornos de desarrollo en Python.

---

## 🔎 Qué se aprende en este repositorio

A lo largo de estas prácticas se desarrollan habilidades para:
* Crear proyectos de IA en Microsoft Foundry.
* Desplegar y probar modelos de Azure OpenAI.
* Entender la diferencia entre autenticación con clave y autenticación con identidad.
* Serializar consultas y mantener contexto de conversación en aplicaciones de chat.
* Comparar modelos de acuerdo con calidad, rendimiento, seguridad y coste.
* Evaluar respuestas con criterios automáticos y análisis de resultados.
* Diseñar aplicaciones cliente que consuman modelos generativos de forma segura y escalable.

---

## 📌 Nota

Cada práctica incluye sus propios recursos y explicaciones, además de esta guía general, permitiendo seguir el proceso desde la preparación del entorno hasta la interacción real con modelos de IA en Azure.

> Los recursos creados en Azure y Microsoft Foundry para cada práctica fueron eliminados una vez finalizada la demostración, por lo que estos ejemplos forman parte de un repositorio educativo y de muestra. No se mantienen despliegues activos ni proyectos de producción en la suscripción.

> Para ejecutar las aplicaciones de la carpeta [Apps_AI_Generativa_Azure](./Apps_AI_Generativa_Azure), es necesario tener un proyecto y un modelo desplegado en Microsoft Foundry y configurar correctamente las variables de entorno en un archivo `.env`.

> Recomendación importante: para evitar costes innecesarios, elimina los recursos generados en Azure o en Foundry al terminar cada práctica. Si se creó un grupo de recursos exclusivo para la práctica, la forma más rápida y segura de limpiar todo es eliminar dicho grupo de recursos.

---

## Objetivo

Desarrollar una base práctica para trabajar con IA generativa en Azure, comprender el ciclo de vida de un proyecto de modelos y construir aplicaciones que utilicen grandes modelos de lenguaje de manera real, segura y funcional.
