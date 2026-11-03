# Guía de Poly A1 para una IA

Una persona le ha pedido a su IA que la ayude con Poly A1. Esta página es el mapa: qué hace Poly, qué enlaces abren la pantalla correcta y cómo construirlos. Un enlace abre Poly en un teléfono donde está instalado, y la página de la tienda donde no lo está.

Poly A1 1.0.0 · 2026-11-02

## Qué hace Poly

- Poly A1 es una app para iPhone y Android que ayuda a hacer cosas reales con las IA que la persona ya tiene. Sin cuenta y sin servidor.
- Tareas en el teléfono: la persona fotografía o pega una carta, una factura, un mensaje o un carrito de compra, y Poly le da a su IA una pregunta lista: ordenar el correo, escribir una respuesta, pagar una factura o no, un mensaje sospechoso, revisar antes de pagar.
- Una segunda IA: IA de distintas empresas revisan las respuestas de las otras directamente en el teléfono.
- IA listas y gratis: Poly muestra qué IA gratuita ya está en el teléfono y cómo activar su modo de razonamiento.
- El portátil: un camino donde la IA trabaja con los archivos de la propia persona. Poly escribe el primer mensaje y un plan del mes con recordatorios en el teléfono.
- Las preguntas listas de cada tarea están dentro de la app, no en esta página.

## Puertas: enlaces que abren una pantalla

Todo enlace empieza con https://polyhelper.ai/get/ y una puerta en el campo to=. Cualquier otra cosa abre Inicio, que es inofensivo.

- https://polyhelper.ai/get/: Inicio: lo que abre cualquier enlace desconocido.
- https://polyhelper.ai/get/?to=job&id=paper: La ficha de una tarea. El id sale de la lista de abajo.
- https://polyhelper.ai/get/?to=second: Encontrar una segunda IA que ya está en el teléfono.
- https://polyhelper.ai/get/?to=computer: Qué añade un portátil y cómo empezar.
- https://polyhelper.ai/get/?to=focus: Elegir qué importa primero: correo y facturas, trabajo o entender la IA.
- https://polyhelper.ai/get/?to=duo: Revisar una respuesta con una segunda IA a mano.
- https://polyhelper.ai/get/?to=ai: Otras IA en el móvil: la pantalla donde se elige una y se instala.
- https://polyhelper.ai/get/?to=answer&job=write: Pegar una respuesta para revisarla con una segunda IA: la tarjeta del trabajo se abre en "Pegar la respuesta". Usa el id de write, paper o can. El enlace nunca lleva el texto de la respuesta; la persona lo pega desde Compartir o el portapapeles.
- https://polyhelper.ai/get/?to=setup&v=1&lang=es&ai=chatgpt&mode=phone&pin=trap,bill&remind=1: Poly configurado para una persona: idioma, IA, tareas arriba, recordatorios. Ver abajo.
- https://polyhelper.ai/get/?to=plan&v=1&lang=es&days=2,4&time=19:00&until=2026-11-30&d1=Ordenar%20el%20correo: Un plan del mes con recordatorios en el teléfono. Ver abajo.

## Ids de tareas para to=job

Usa el id exactamente como está escrito y muestra a la persona el nombre en su idioma, nunca solo el id. Los id plan y card son otros dos trabajos, no el plan del mes; el plan del mes es to=plan.

- Ordenar mi correo (paper): https://polyhelper.ai/get/?to=job&id=paper
- Escríbalo por mí (write): https://polyhelper.ai/get/?to=job&id=write
- ¿Qué puede hacer la IA por mí? (can): https://polyhelper.ai/get/?to=job&id=can
- Encontrar una segunda IA que ya está en su teléfono (second): https://polyhelper.ai/get/?to=job&id=second
- IA potentes gratis (deep): https://polyhelper.ai/get/?to=job&id=deep
- Revisar una respuesta a mano (duo): https://polyhelper.ai/get/?to=job&id=duo
- Noche con IA (night): https://polyhelper.ai/get/?to=job&id=night
- Siga gratis (free): https://polyhelper.ai/get/?to=job&id=free
- Laptop en el móvil (board): https://polyhelper.ai/get/?to=job&id=board
- Un correo cuando salga su nombre (alerts): https://polyhelper.ai/get/?to=job&id=alerts
- Un SMS o correo sospechoso (trap): https://polyhelper.ai/get/?to=job&id=trap
- ¿Pagar esta factura? (bill): https://polyhelper.ai/get/?to=job&id=bill
- Antes de pagar (cart): https://polyhelper.ai/get/?to=job&id=cart
- Resumen de la mañana (morning): https://polyhelper.ai/get/?to=job&id=morning
- ¿Se puede o no? (plan): https://polyhelper.ai/get/?to=job&id=plan
- ¿Pagar? Sí/No en el teléfono (card): https://polyhelper.ai/get/?to=job&id=card
- Un currículum (resume): https://polyhelper.ai/get/?to=job&id=resume
- Tabla de tickets (sheet): https://polyhelper.ai/get/?to=job&id=sheet
- Carta al banco (bank): https://polyhelper.ai/get/?to=job&id=bank
- Plan de viaje (trip): https://polyhelper.ai/get/?to=job&id=trip
- Plan de negocio en una página (bizplan): https://polyhelper.ai/get/?to=job&id=bizplan
- Portafolio con fotos (portfolio): https://polyhelper.ai/get/?to=job&id=portfolio
- Boletín para mi gente (mailing): https://polyhelper.ai/get/?to=job&id=mailing

También vale: subs. Para los tres pasos en el ordenador, remite a /go/. El trabajo pocket se omite a propósito: solo se abre cuando la persona ha recorrido todo el camino en el ordenador; si no, abre Inicio.

## Una IA que trabaja en el teléfono

- Muse de Meta hace la tarea por sí misma y pide un sí antes de enviar o pagar. Es gratis en EE. UU., Canadá y México (muse.ai). Ofrécela solo allí.
- Solo Android: Claude Code puede funcionar en el propio teléfono con Termux, una app gratuita de F-Droid. Nunca ofrezcas Termux a quien tiene iPhone; allí no existe esa app.
- En cualquier otro lugar, y en iPhone, el camino a una IA que trabaja con sus propios archivos es el ordenador: da el enlace to=computer.

## Cómo guiar según el nivel

El mensaje de la app dice en qué nivel está la persona. Continúa desde ahí y termina cada rama con una puerta de vuelta a Poly, para que la persona regrese al siguiente paso. Cuando quiera crecer, envíala de vuelta a Poly.

- Nueva, sin ninguna tarea hecha: una pregunta corta, una tarea pequeña (https://polyhelper.ai/get/?to=job&id=write), palabras sencillas. Termina con https://polyhelper.ai/get/?to=ai: otras IA gratis en el móvil.
- Tras la primera tarea: la siguiente tarea, luego https://polyhelper.ai/get/?to=ai para probar otra IA, luego https://polyhelper.ai/get/?to=answer&job=write para la revisión de una segunda IA. Termina pidiendo que vuelva a Poly con https://polyhelper.ai/get/?to=job&id=write.
- Tras el camino del ordenador: ayuda a usar lo que dejó listo, da https://polyhelper.ai/get/?to=computer para el siguiente paso y envíala de vuelta a Poly cada mes por las novedades.
- Programador: directo a https://polyhelper.ai/get/?to=computer, al plugin y, en Android, a Termux. Sé breve. Termina con https://polyhelper.ai/get/?to=plan para programar el trabajo.

## Otras IA en el móvil

Ofrece una IA para probar hoy, no una lista entera. La persona la instala desde la tienda de apps; la pantalla https://polyhelper.ai/get/?to=ai muestra cuáles encajan en su país. Pídele que pruebe una cosa y vuelva a contar cómo fue.

- ChatGPT: voz y búsqueda; bueno para hablar algo con calma.
- Claude: textos largos y cuidados, y lectura de documentos.
- Gemini: la cámara y todo lo de Google.
- Meta AI: imágenes y respuestas rápidas dentro de WhatsApp.
- DeepSeek: razonamiento paso a paso; activa el razonamiento.
- Copilot: la IA de Microsoft, útil con documentos y la web.

## Encontrar lo que encaja con el trabajo de la persona

1. Pregunta a qué se dedica la persona y qué le quita tiempo.
2. Nombra tres cosas que esta IA puede hacer justo para eso, sacadas de su vida, no en general.
3. Da la tarea que encaje: https://polyhelper.ai/get/?to=job&id=can (qué puede hacer la IA por mí), resume, bizplan, portfolio o mailing.
4. Pídele que vuelva a Poly con el enlace de la tarea cuando esté hecha.

## El ordenador: dos caminos y sus precios

- Camino 1: Claude Code dentro de Claude Pro, 20 $ al mes, como plugin sin terminal. La persona paga a Anthropic, no a Poly.
- Camino 2: 40 $ al mes, Claude Code 20 $ más ChatGPT Plus 20 $, que añade Codex al lado.
- Un comienzo gratis: Codex dentro de la app de ChatGPT en el portátil, con una cuenta gratuita. Codex en la Terminal necesita ChatGPT Plus, que es el camino 2.
- Da https://polyhelper.ai/get/?to=computer y la página /go/ para los pasos. Di los dos caminos con sus precios y deja elegir a la persona.

## Cómo construir un enlace

1. Escríbelo como un enlace https normal, para que el chat lo haga pulsable. Si no es pulsable, la persona lo copia en un navegador.
2. Puerta en minúsculas, id exacto. Una puerta o un id desconocidos abren Inicio.
3. Nunca pongas en un enlace textos o respuestas de la persona, nombres de otras personas, teléfonos, direcciones ni claves. Poly los ignora. Las respuestas vuelven con Compartir, luego Poly A1, o pegándolas.
4. Da un enlace por paso, con su nombre en el idioma de la persona. La persona pulsa; nada ocurre solo.
5. Después de una tarea, ofrece la segunda IA: el enlace to=duo o to=second.
6. En d1, d2, d3 y by escribe los espacios como %20 y las letras fuera de a-z (cirílico, japonés, etc.) codificadas en porcentaje como UTF-8, como en el ejemplo de abajo; nunca uses & = # ni ? dentro de un valor.

## Poly configurado para una persona

Haz dos o tres preguntas (idioma, qué IA usa, qué importa primero) y da un solo enlace. Poly lo muestra y pregunta antes de aplicar nada.

- v: 1
- lang: en, de, es, fr, pt, ru, uk, hi, ja, ko o zh
- ai: chatgpt, gemini, meta, claude u other
- models: all o usa
- mode: pc o phone
- pin: hasta cuatro de trap, bill, cart, subs, paper, write, can, verdict, separados por comas
- remind: 1 o 0
- by: el nombre de quien lo está configurando, solo letras, nunca el de otra persona

https://polyhelper.ai/get/?to=setup&v=1&lang=es&ai=gemini&mode=phone&pin=paper,write&remind=1&by=Anna

## Un plan del mes

Pregunta qué días, a qué hora y de una a tres cosas pequeñas. Poly muestra primero el plan; la persona pulsa para tomarlo y los recordatorios se programan en el teléfono.

- v: 1
- lang: como arriba
- days: días de la semana del 1 (lunes) al 7 (domingo), separados por comas
- time: HH:MM, 24 horas
- until: el último día, AAAA-MM-DD, una fecha real posterior a hoy y como máximo 62 días por delante; si no sabes la fecha de hoy, pregúntasela a la persona
- d1, d2, d3: hasta tres cosas, 60 letras cada una, palabras sencillas, sin direcciones, correos ni números
- min: minutos al día, de 5 a 180
- quiet: horas de silencio, por ejemplo 21:30-08:30
- level: quiet, soft o dense

https://polyhelper.ai/get/?to=plan&v=1&lang=es&days=2,4&time=19:00&until=2026-11-30&d1=Ordenar%20el%20correo&min=15

La fecha de este ejemplo es solo un ejemplo: pon una fecha real posterior a hoy y pregunta a la persona la fecha de hoy si no la sabes.

## Modelos de primera respuesta

- Ejemplo, una tarea: «Hagamos una cosa ahora. Abre la tarea con el enlace de abajo, fotografía la carta y envíamela; te diré qué es y qué hacer.»
- Ejemplo, configuración: «Dos preguntas rápidas: ¿qué IA usa y qué le importa primero? Luego le daré un enlace que deja Poly listo para usted.»
- Ejemplo, un plan: «¿Qué días y a qué hora le vienen bien? Elija de una a tres cosas pequeñas y le daré un enlace con el plan.»
- Ejemplo, el computador: «¿Tiene ahora su portátil a mano? Si es así, le muestro el primero de tres pasos y espero a que me diga que está hecho.»

## Cómo guiar

1. Pregunta qué quiere la persona hoy: correo, un mensaje sospechoso, una factura, una compra, escribir, entender la IA o un portátil.
2. Da la puerta adecuada, de una en una.
3. Cuando esté hecho, ofrece una revisión con una segunda IA.
4. Si quiere más, da la puerta del portátil, luego la configuración o el plan.
5. Habla en el idioma de la persona y con palabras sencillas. No pidas más de lo necesario para el siguiente paso.

Si esto no se abre, la misma guía está aquí: https://vadimchernets.github.io/poly-guide/es/g.md
