# Guía de Poly A1 para una IA

Poly A1 1.0.0 · 2026-11-02

## Cómo guiar según el nivel

Programador: directo a https://polyhelper.ai/get/?to=computer, al plugin y, en Android, a Termux. Sé breve. Termina con https://polyhelper.ai/get/?to=plan para programar el trabajo.

## Puertas: enlaces que abren una pantalla

Todo enlace empieza con https://polyhelper.ai/get/ y una puerta en el campo to=. Cualquier otra cosa abre Inicio, que es inofensivo.

- https://polyhelper.ai/get/?to=job&id=paper: La ficha de una tarea. El id sale de la lista de abajo.
- https://polyhelper.ai/get/?to=ai: Otras IA en el móvil: la pantalla donde se elige una y se instala.
- https://polyhelper.ai/get/?to=answer&job=write: Pegar una respuesta para revisarla con una segunda IA: la tarjeta del trabajo se abre en "Pegar la respuesta". Usa el id de write, paper o can. El enlace nunca lleva el texto de la respuesta; la persona lo pega desde Compartir o el portapapeles.
- https://polyhelper.ai/get/?to=second: Encontrar una segunda IA que ya está en el teléfono.
- https://polyhelper.ai/get/?to=computer: Qué añade un portátil y cómo empezar.
- https://polyhelper.ai/get/?to=focus: Elegir qué importa primero: correo y facturas, trabajo o entender la IA.

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

https://polyhelper.ai/es/g/g.md
