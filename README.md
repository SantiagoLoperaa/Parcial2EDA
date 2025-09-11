DOCUMENTACIÓN USADA - PARCIAL #2 EDA

Profe, en este intento de solución implementé estructuras de datos, recursividad, listas enlazadas y consumo de API en Python.  
Por eso, para respaldar un poquito de donde saqué las herramientas para presentar esta solución, a continuación, te dejo los links de documentación oficial y de referencia de las opciones que encontré para realizar este parcial

----Fase #1----
Enlaces de documentación

Python – Conceptos básicos
- [Clases en Python (`class`, `__init__`)](https://docs.python.org/3/tutorial/classes.html)
- [Funciones en Python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Recursividad en Python (Tutorial oficial)](https://docs.python.org/3/tutorial/controlflow.html#recursion)

Estructuras de datos
- [Listas enlazadas en Python (concepto general)](https://realpython.com/linked-lists-python/)
- [Colecciones – `deque`](https://docs.python.org/3/library/collections.html#collections.deque)

Manipulación de strings
- [Método `.join()`](https://docs.python.org/3/library/stdtypes.html#str.join)
- [Función `ord()` y `chr()`](https://docs.python.org/3/library/functions.html#ord)

Librerías externas
- [Requests – `requests.get()`](https://requests.readthedocs.io/en/latest/user/quickstart/)

Conceptos adicionales
- [Docstrings en Python](https://peps.python.org/pep-0257/)
- [Métodos especiales de objetos (`__str__`, `__repr__`)](https://docs.python.org/3/reference/datamodel.html#object.__repr__)

Consumo de API y ayuda en organización de clases en carpetas model, services, main:
-[ChatGPT](https://chatgpt.com/)

Nota:
Estos enlaces respaldan cada una de las técnicas, librerías y estructuras utilizadas en la implementación de la Fase 1 de este parcial.


-----Fase 2 – Proceso de Desencriptación y Logs-----

En esta fase se implementó la desencriptación de frases (inverso del proceso de encriptación) y la incorporación de logs especializados para sistema, tiempos y performance.

Funcionalidades

Desencriptación

Extraer desde el ArrayDeque las listas enlazadas.

Revertir la rotación de nodos (iterativa y recursiva).

Restar los números impares consecutivos a los valores ASCII.

Reconstruir el mensaje original.

Logs implementados

Logs de sistema → seguimiento detallado de cada método (inicio y fin de procesos).

Logs de tiempos → mediciones en milisegundos de encriptación y desencriptación.

Logs de performance → métricas de memoria, CPU y número de threads con psutil.

Todos los logs se guardan automáticamente en la carpeta logs/ en los archivos:

sistema.log

tiempos.log

performance.log

Documentación oficial utilizada

Logging (Python) → https://docs.python.org/3/library/logging.html

time — Time access and conversions → https://docs.python.org/3/library/time.html

collections.deque → https://docs.python.org/3/library/collections.html#collections.deque

psutil – System and process utilities → https://psutil.readthedocs.io/en/latest/
