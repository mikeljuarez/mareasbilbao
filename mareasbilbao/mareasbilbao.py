import requests
import json

class mareasbilbao:
    def __init__(self, fecha:int, url = "https://ideihm.covam.es/api-ihm/getmarea?request=gettide&id=2&format=json&date="):
        if len(str(fecha)) == 8:
            self.fecha = fecha
            self.url = url + fecha
        else:
            raise 
        response = requests.get(self.url)
        datos = json.loads(response.text)
        self.datos = datos['mareas']['datos']['marea']

    def horario(self):
        for x in self.datos:
            print(x['hora'], x['tipo'])
        return "¡Gracias por usar nuestra API!"

