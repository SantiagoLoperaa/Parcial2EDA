from services.api import ApiFrases
from model.frase import Frase

def main():
    url = "https://zenquotes.io/api/quotes"
    clienteApi = ApiFrases(url)

    frases = clienteApi.obtenerFrases()
    if not frases:
        print("No se pudieron obtener frases desde la API.")
        return

    print(f"Se obtuvieron {len(frases)} frases de la API.\n")

    for i, texto in enumerate(frases, start=1):
        print(f"--- Frase {i} ---")
        print("Original:")
        print(texto)

        # Encriptar iterativo
        f = Frase(texto)
        f.encriptarTodoIterativo()
        print("\nEncriptado (iterativo):")
        print(f.obtenerEncriptado())

        print("Desencriptado (iterativo):")
        print(f.desencriptarTodoIterativo())

        # Encriptar recursivo
        f2 = Frase(texto)
        f2.encriptarTodoRecursivo()
        print("\nEncriptado (recursivo):")
        print(f2.obtenerEncriptado())

        print("Desencriptado (recursivo):")
        print(f2.desencriptarTodoRecursivo())

        print("\n")

if __name__ == "__main__":
    main()
