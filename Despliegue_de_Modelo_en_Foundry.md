# Creación de un proyecto en Microsoft Foundry

En esta práctica crearás un proyecto de Microsoft Foundry y lo explorarás en el portal de Foundry.
También explorarás la extensión Foundry Toolkit para VS Code, que ofrece una forma práctica de trabajar con proyectos de Foundry y sus recursos.

Esta parte es importante porque, antes de implementar cualquier aplicación, chat, agente o solución de IA, debes crear un proyecto de Foundry. Este es el primer paso para comenzar cualquier proyecto relacionado con chatbots o agentes de IA.

**Recomendación:** Para evitar costes innecesarios, al terminar esta práctica o cualquier otra, elimina los recursos que se hayan creado en tu cuenta de Azure. Puedes eliminar el grupo de recursos completo si utilizas uno exclusivo para esta práctica; esta es una manera más rápida y eficiente de eliminarlo todo.

---

Antes de comenzar este proceso, debes tener lo siguiente:

- Una suscripción activa de Azure.
- Visual Studio Code instalado.
- Git instalado y configurado para el control de versiones.
- Azure CLI instalado.
- Python 3.13.12 instalado.

## Requisitos previos

1. En tu navegador web, abre el [portal de Microsoft Foundry](https://ai.azure.com) e inicia sesión con tus credenciales de Azure.

2. Si aún no está habilitada, activa la opción **New Foundry** en la barra de herramientas situada en la parte superior de la página. A continuación, crea un proyecto con un nombre único y expande el área de **Opciones avanzadas** para especificar la siguiente información:
    - **Recurso de Foundry:** utiliza el nombre predeterminado para el recurso.
    - **Suscripción:** selecciona tu suscripción de Azure.
    - **Grupo de recursos:** crea o selecciona un grupo de recursos.
    - **Región:** selecciona una de las regiones **recomendadas por AI Foundry** en la lista. Anota la región seleccionada, ya que la necesitarás más adelante.

3. Selecciona **Crear** y espera a que se cree el proyecto. Cuando esté listo, se abrirá la página principal del proyecto.

---

## Implementar y probar un modelo

1. Ahora podrás explorar los modelos. En la página **Descubrir**, selecciona la pestaña **Modelos** para ver el catálogo de modelos de Microsoft Foundry.

2. Busca el modelo **gpt-5.2** y selecciónalo en los resultados de la búsqueda para consultar su ficha técnica.
Cada modelo contiene su propia ficha técnica, que proporciona información para ayudarte a comprender sus capacidades y limitaciones, y a determinar si se ajusta a tus necesidades.

3. Selecciona **Implementar** con la configuración predeterminada para crear una implementación del modelo.
Las implementaciones de modelos te permiten trabajar con un modelo en tu proyecto. Una vez implementado el modelo, el entorno de pruebas se abrirá automáticamente para que puedas probarlo.

4. En el cuadro de **Instrucciones**, introduce una o varias instrucciones. Por ejemplo:
    *Eres un asistente de IA que puede dar recomendaciones sobre desarrollo de software.*

5. En la ventana de chat, introduce una consulta (*prompt*). Por ejemplo:
    *Describe los tres patrones de diseño más utilizados.*

---

## Puntos de conexión de los recursos y proyectos de Microsoft Foundry

1. En el portal de Foundry, selecciona **Gestionar** en la barra de menú superior.
El centro de administración es donde puedes ver y gestionar tus proyectos y sus recursos principales:
    - El **nivel de recursos** se refiere al recurso de Foundry creado en Azure para dar soporte a tu proyecto. Este recurso incluye conexiones a los servicios y modelos de Foundry, y proporciona un lugar centralizado para gestionar el acceso de los usuarios a los proyectos de desarrollo de IA.
    - El **nivel de proyecto** se refiere a tu proyecto individual, donde puedes agregar y administrar recursos específicos. Un recurso puede dar soporte a varios proyectos. El primero que se crea es el **proyecto predeterminado** del recurso.

2. Selecciona el enlace al **recurso principal** asociado con el proyecto.
Se deben mostrar los detalles de configuración del recurso.
Ten en cuenta que el recurso de Foundry tiene un punto de conexión a través del cual las aplicaciones cliente pueden acceder a la funcionalidad a nivel de recurso, como las herramientas de Foundry que se comparten entre todos los proyectos del recurso.

3. En la barra de menú superior, selecciona **Inicio** para volver a la página principal del proyecto.

4. Ten en cuenta la **clave**, el **punto de conexión del proyecto** y el **punto de conexión** de Azure OpenAI.
Esta información se utiliza para conectarte con los recursos de tu proyecto desde las aplicaciones cliente.
    - La **clave** se utiliza para la autenticación basada en claves en modelos y herramientas. Sin embargo, en la mayoría de los escenarios de producción deberías considerar el uso de la autenticación de Microsoft Entra ID, basada en identidades de usuario y de aplicaciones autenticadas.
    - El **punto de conexión del proyecto** se utiliza para acceder a los modelos proporcionados directamente en Foundry, incluidos los modelos de OpenAI, mediante la **API de OpenAI Responses**, y para acceder a las API específicas de Foundry, como el servicio **Foundry Agent**.
    - El **punto de conexión de OpenAI** se utiliza para acceder a los modelos mediante las **API de OpenAI**, incluidas la **API de finalización de chat** y la **API de respuestas**.

---

## Instalar la extensión Foundry Toolkit para Visual Studio Code

Como desarrollador, es posible que dediques tiempo a trabajar en el portal de Foundry, pero también es probable que pases mucho tiempo en Visual Studio Code. La extensión Foundry Toolkit te ofrece una forma práctica de trabajar con los recursos del proyecto de Foundry sin salir del entorno de desarrollo.

1. Abre Visual Studio Code.

2. En la barra de navegación, normalmente situada en el lado izquierdo, selecciona **Extensiones**.

3. Busca **Foundry Toolkit** en el mercado de extensiones e instala la extensión **Foundry Toolkit para VS Code**.

4. Tras instalar la extensión, selecciona la página **Foundry Toolkit** en la barra de navegación y espera a que se cargue.

5. En el panel Foundry Toolkit, expande **Recursos de Microsoft Foundry** y configura el proyecto predeterminado conectándote a Azure. Inicia sesión con tus credenciales y selecciona el proyecto de Foundry que creaste anteriormente.

6. Tras configurar el proyecto predeterminado, expande el proyecto, expande **Modelos** y selecciona el modelo **gpt-5.2** que implementaste previamente.
Aquí puedes consultar los detalles de la implementación del modelo.

7. En el panel de Foundry Toolkit, en la sección **Herramientas para desarrolladores**, expande **Compilación** y selecciona el modelo **gpt-5.2**, en caso de que aún no esté seleccionado.
En VS Code se abrirá un entorno interactivo donde podrás probar el modelo.


