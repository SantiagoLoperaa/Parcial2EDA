"""FASE #1"""
"""from collections import deque
from model.listaenlazada import ListaEnlazada

class Frase:
    def __init__(self, textoOriginal):
        self.textoOriginal = textoOriginal
        self.colaPalabras = deque()
        self.textoEncriptado = None

    def _encriptarPalabraALista(self, palabra):
        lista = ListaEnlazada()
        impar = 1
        for caracter in palabra:
            valor = ord(caracter) + impar
            lista.insertarFinal(valor)
            impar += 2
        return lista

    def _construirRepresentacionEncriptada(self):
        return " ".join("[" + ",".join(str(x) for x in lista.aLista()) + "]" for lista in self.colaPalabras)


    def encriptarTodoIterativo(self):
        self.colaPalabras.clear()
        palabras = self.textoOriginal.split(" ")
        for palabra in palabras:
            lista = self._encriptarPalabraALista(palabra)
            lista.rotarLista()
            self.colaPalabras.append(lista)
        self.textoEncriptado = self._construirRepresentacionEncriptada()

    def encriptarTodoRecursivo(self):
        self.colaPalabras.clear()
        palabras = self.textoOriginal.split(" ")
        for palabra in palabras:
            lista = self._encriptarPalabraALista(palabra)
            lista.rotarListaRec()
            self.colaPalabras.append(lista)
        self.textoEncriptado = self._construirRepresentacionEncriptada()

    def obtenerEncriptado(self):
        return self.textoEncriptado

    def desencriptarTodoIterativo(self):
        palabras = []
        for lista in self.colaPalabras:
            lista.rotarLista()
            impar = 1
            palabra = ""
            for valor in lista.aLista():
                asciiOriginal = valor - impar
                palabra += chr(asciiOriginal)
                impar += 2
            palabras.append(palabra)
        return " ".join(palabras)

    def desencriptarTodoRecursivo(self):
        palabras = []
        for lista in self.colaPalabras:
            lista.rotarListaRec()
            impar = 1
            palabra = ""
            for valor in lista.aLista():
                asciiOriginal = valor - impar
                palabra += chr(asciiOriginal)
                impar += 2
            palabras.append(palabra)
        return " ".join(palabras)"""


"""FASE #2"""
from collections import deque
from model.listaenlazada import ListaEnlazada
from services.loggerConfiguracion import loggerSistema, loggerTiempos, loggerPerformance
from services.performanceMonitor import loggear_metricas
import time

class Frase:
    def __init__(self, textoOriginal):
        self.textoOriginal = textoOriginal
        self.colaPalabras = deque()
        self.textoEncriptado = None

    def _encriptarPalabraALista(self, palabra):
        lista = ListaEnlazada()
        impar = 1
        for caracter in palabra:
            valor = ord(caracter) + impar
            lista.insertarFinal(valor)
            impar += 2
        return lista

    def _construirRepresentacionEncriptada(self):
        return " ".join("[" + ",".join(str(x) for x in lista.aLista()) + "]" for lista in self.colaPalabras)

    # --- Encriptar Iterativo ---
    def encriptarTodoIterativo(self):
        loggerSistema.info("Iniciando encriptación iterativa")
        t0 = time.perf_counter_ns()
        self.colaPalabras.clear()

        for palabra in self.textoOriginal.split(" "):
            lista = self._encriptarPalabraALista(palabra)
            lista.rotarLista()
            self.colaPalabras.append(lista)

        self.textoEncriptado = self._construirRepresentacionEncriptada()
        t1 = time.perf_counter_ns()
        loggerTiempos.info(f"Tiempo encriptación iterativa: {(t1-t0)//1_000_000} ms")
        loggear_metricas(loggerPerformance, etiqueta="encriptacion_iterativa")
        loggerSistema.info("Finalizó encriptación iterativa")

    # --- Encriptar Recursivo ---
    def encriptarTodoRecursivo(self):
        loggerSistema.info("Iniciando encriptación recursiva")
        t0 = time.perf_counter_ns()
        self.colaPalabras.clear()

        for palabra in self.textoOriginal.split(" "):
            lista = self._encriptarPalabraALista(palabra)
            lista.rotarListaRec()
            self.colaPalabras.append(lista)

        self.textoEncriptado = self._construirRepresentacionEncriptada()
        t1 = time.perf_counter_ns()
        loggerTiempos.info(f"Tiempo encriptación recursiva: {(t1-t0)//1_000_000} ms")
        loggear_metricas(loggerPerformance, etiqueta="encriptacion_recursiva")
        loggerSistema.info("Finalizó encriptación recursiva")

    def obtenerEncriptado(self):
        return self.textoEncriptado

    # --- Desencriptar Iterativo ---
    def desencriptarTodoIterativo(self):
        loggerSistema.info("Iniciando desencriptación iterativa")
        t0 = time.perf_counter_ns()

        palabras = []
        for lista in self.colaPalabras:
            lista.rotarLista()
            impar = 1
            palabra = ""
            for val in lista.aLista():
                palabra += chr(val - impar)
                impar += 2
            palabras.append(palabra)

        mensaje = " ".join(palabras)
        t1 = time.perf_counter_ns()
        loggerTiempos.info(f"Tiempo desencriptación iterativa: {(t1-t0)//1_000_000} ms")
        loggear_metricas(loggerPerformance, etiqueta="desencriptacion_iterativa")
        loggerSistema.info("Finalizó desencriptación iterativa")
        return mensaje

    # --- Desencriptar Recursivo ---
    def desencriptarTodoRecursivo(self):
        loggerSistema.info("Iniciando desencriptación recursiva")
        t0 = time.perf_counter_ns()

        palabras = []
        for lista in self.colaPalabras:
            lista.rotarListaRec()
            impar = 1
            palabra = ""
            for val in lista.aLista():
                palabra += chr(val - impar)
                impar += 2
            palabras.append(palabra)

        mensaje = " ".join(palabras)
        t1 = time.perf_counter_ns()
        loggerTiempos.info(f"Tiempo desencriptación recursiva: {(t1-t0)//1_000_000} ms")
        loggear_metricas(loggerPerformance, etiqueta="desencriptacion_recursiva")
        loggerSistema.info("Finalizó desencriptación recursiva")
        return mensaje
