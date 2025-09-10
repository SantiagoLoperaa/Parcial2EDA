from services.api import ApiFrases
from model.frase import Frase

def main():
    url = "https://zenquotes.io/api/quotes"
    clienteApi = ApiFrases(url)

    frases = clienteApi.obtenerFrases()
    if not frases:
        print("No se pudieron obtener frases desde la API.")
        return

    texto = frases[0]
    print("Frase original de la API:")
    print(texto)
    print()

    # Encriptar iterativo
    f = Frase(texto)
    f.encriptarTodoIterativo()
    print("Texto encriptado (iterativo):")
    print(f.obtenerEncriptado())
    print()
    print("Texto desencriptado (iterativo):")
    print(f.desencriptarTodoIterativo())
    print()

    # Encriptar recursivo
    f2 = Frase(texto)
    f2.encriptarTodoRecursivo()
    print("Texto encriptado (recursivo):")
    print(f2.obtenerEncriptado())
    print()
    print("Texto desencriptado (recursivo):")
    print(f2.desencriptarTodoRecursivo())

if __name__ == "__main__":
    main()
