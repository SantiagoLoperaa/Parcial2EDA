import requests

class APIFrases:
    def __init__(self, url):
        self.url = url
        
    def obtener_frases(self):
        try:
            respuesta = requests.get(self.url)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                #Acá se extrae solo el texto de la frase ("q") <-- Así lo denomina la documentación de la API.
                return [item["q"] for item in datos]
            else:
                return []
        except Exception as e:
            print(f"Error al conectarse con la API: {e}")
            return []
        