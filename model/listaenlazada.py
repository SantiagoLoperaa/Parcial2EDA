from model.nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertarFinal(self, dato):
        nuevoNodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevoNodo
            return
        ultimo = self.cabeza
        while ultimo.siguiente:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevoNodo

    def aLista(self):
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def rotarLista(self):
        nodoAux = Nodo(0)
        nodoAux.siguiente = self.cabeza
        previo = nodoAux
        while previo.siguiente and previo.siguiente.siguiente:
            primero = previo.siguiente
            segundo = primero.siguiente

            # Reenlazar
            previo.siguiente = segundo
            primero.siguiente = segundo.siguiente
            segundo.siguiente = primero

            previo = primero
        self.cabeza = nodoAux.siguiente

    # --- Rotación recursiva ---
    def _rotarRec(self, nodo):
        if not nodo or not nodo.siguiente:
            return nodo
        primero = nodo
        segundo = nodo.siguiente
        primero.siguiente = self._rotarRec(segundo.siguiente)
        segundo.siguiente = primero
        return segundo

    def rotarListaRec(self):
        self.cabeza = self._rotarRec(self.cabeza)
