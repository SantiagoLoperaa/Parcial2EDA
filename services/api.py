import requests

class ApiFrases:
    def __init__(self, url):
        self.url = url
        
    def obtenerFrases(self):
        try:
            respuesta = requests.get(self.url)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                return [item["q"] for item in datos]
            else:
                return []
        except Exception as e:
            print(f"Error al conectarse con la API: {e}")
            return []

        