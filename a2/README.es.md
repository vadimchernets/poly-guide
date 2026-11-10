# Poly A2

Ayuda ahora, crecer con trabajo útil. Empieza en la IA que la persona ya usa, pega una instrucción autónoma de Poly A2 y continúa con la tarea real de la persona. La guía es una referencia para la IA que ayuda, no un curso obligatorio ni una razón para enviar cada respuesta de vuelta a una app.

- [Guía](guide.md) / [Guía en ruso](guide.ru.md)
- [Fuentes revisadas y límites de las capacidades](sources.md)
- [Instrucciones generadas a partir del código fuente de la aplicación](prompts/)
- [Preferencias opcionales del proyecto y tarjeta de continuación](templates/)
- [Tres puntos de control en la computadora y primera tarea real](templates/DESKTOP-PATH.md)
- [Dos IA en una ventana de la computadora](templates/TEAM-ONE-WINDOW.md)
- [Duo para el teléfono: proyecto independiente y configuración actual](https://github.com/vadimchernets/poly-duo)
- Entrada de Poly A2: https://polyhelper.ai/a2/
- Guía del sitio web: https://polyhelper.ai/g/a2.md
- Espejo: https://raw.githubusercontent.com/vadimchernets/poly-guide/main/a2/guide.md

La ruta de la computadora distingue entre abrir el entorno de trabajo, comprobar el acceso a archivos con la sesión iniciada y un primer resultado real confirmado por la persona. Después, un Claude Code/Codex principal compatible puede usar el otro CLI instalado y recibir su resultado real de revisión en la misma ventana. Poly A2 prepara la tarea; no ejecuta ni inspecciona esa terminal. Duo para el teléfono es externo y depende de la plataforma; abrir su atajo no prueba ningún resultado.

Los mensajes de configuración, primera tarea y una sola ventana para ambas herramientas de la computadora se generan directamente desde la aplicación junto con las instrucciones principales completas. Consulta `prompts/index.json` para ver las funciones de origen y el SHA-256 de cada archivo. Publicar el paquete es una acción del propietario, no un efecto secundario de generarlo.

Este directorio `a2/` es un paquete de publicación aditivo. No reemplaza otro material de este repositorio. Las funciones de los servicios externos dependen de la cuenta, el dispositivo, la región y los permisos reales. No se promete uso ilimitado, memoria permanente, control automático de la terminal ni publicación en una tienda de apps.

---
