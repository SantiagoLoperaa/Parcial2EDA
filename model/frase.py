from collections import deque
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
        return " ".join(palabras)
