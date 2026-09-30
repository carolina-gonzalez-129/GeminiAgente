---
name: aplicar-plantillas
description: Identifica si una entrada corresponde a un instructivo o una solución y la organiza usando la plantilla Instructivo o Soluciones de Finnegans.
---

# Aplicar plantillas

Usa esta skill para organizar un texto nuevo o existente como artículo de la Base de Conocimiento. El tipo de plantilla es un dato obligatorio de entrada. Aplica únicamente el formato solicitado. Esta skill es independiente: no invoca otras skills.

## Datos obligatorios de entrada

La solicitud debe incluir:

- **Título**
- **Categoría**
- **Tipo de plantilla:** exactamente `instructivo` o `soluciones`
- **Contenido fuente**
- **Etiquetas temáticas**, si existen

Si falta el tipo, no lo infieras ni apliques una plantilla: solicita ese dato. Si falta otro dato, conserva un marcador `[Indicar ...]` únicamente cuando sea posible estructurar el artículo sin inventar información.

## Aplicación

- Para `instructivo`, usa [la plantilla Instructivo](references/plantilla-instructivo.md) y consulta por defecto el ejemplo de [Bot de Granos](references/ejemplo-instructivo.md). El ejemplo de [Unidades de Compra](references/ejemplo-instructivo-unidades-compra.md) es opcional y contiene además un texto original extenso.
- Para `soluciones`, usa [la plantilla de Soluciones](references/plantilla-soluciones.md) y consulta el [ejemplo de Nota de Crédito de Ventas](references/ejemplo-soluciones.md).
- Para verificar el comportamiento, usa [los casos de prueba](references/casos-de-prueba.md).
- Conserva el orden y los nombres de las secciones de la plantilla elegida.
- Devuelve siempre este encabezado, en este orden:

  **Título:** [título recibido]  
  **Categoría:** [categoría recibida]  
  **Tipo de plantilla:** instructivo o soluciones  
  **Etiquetas:** [tipo obligatorio y etiquetas temáticas recibidas]

  Después del encabezado, devuelve únicamente el cuerpo publicable del artículo. No agregues comentarios editoriales, observaciones, diagnósticos ni estados de revisión.
- No inventes categorías, rutas, pantallas, causas, mensajes, datos, acciones, resultados ni capacidades del sistema.
- Si falta información, conserva un marcador claro como `[Indicar ruta]` dentro de la sección correspondiente, o pide el dato si impide estructurar el artículo.
- En la plantilla Instructivo, incluye **Qué hace y qué no hace** cuando se describa el alcance o comportamiento de una funcionalidad. Usa solo capacidades y límites confirmados; si faltan, déjalos señalados como pendientes.
- En Soluciones, estructura el cuerpo con **Consulta** seguido de **Pasos a seguir**. Dentro de **Consulta**, después de describir el problema, añade un párrafo breve sobre la causa y cómo solucionarlo únicamente si está confirmado. No agregues un encabezado separado **Respuesta**.
- Escribe las acciones y pasos con verbos en infinitivo.
- El tiempo de lectura no forma parte de la salida del modelo. Si la aplicación lo necesita, debe calcularlo fuera de la skill a partir de la cantidad de palabras.
- No incluyas instrucciones sobre botones de edición, Paint, colores de marca, publicación ni otras pautas editoriales en el artículo.
- No incluyas una sección **Requiere AppBuilder** salvo que la solicitud proporcione explícitamente ese dato y el formato de integración la requiera.

## Etiquetas

Las etiquetas deben incluir siempre el tipo correspondiente:

- `instructivo` para la plantilla Instructivo.
- `soluciones` para la plantilla Soluciones.

Conserva las etiquetas temáticas recibidas y no inventes etiquetas adicionales, salvo la etiqueta obligatoria del tipo. Usa siempre la forma `soluciones`, también cuando el texto fuente diga “Solución”.
