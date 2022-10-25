# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = {
                "Nombre": "Edwin",
                "Apellido": "Yepez",
                "DNI": "152329",
                "Vestir": [
                        {
                            "prenda": "camisa",
                            "cantidad": 12
                        },
                        {
                            "prenda": "pantalon",
                            "cantidad": 8
                        },
                        {
                            "prenda": "chaqueta",
                            "cantidad": 4
                        }
                        ]
                }
    # print(json_data)
    with open ('edwin_json.json', 'w') as archivo_json:
        datos = [json_data]
        json.dump(datos, archivo_json, indent=4)
        

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()
    json_data = {"Autos": "mazda", "motocicletas": "yamaha"}
    
    with open('edwin_json.json', 'r') as otro_json:
        nueva_data = json.load(otro_json)
        nueva_data.append(json_data)

    with open('edwin_json.json', 'w') as otro_json:
        json.dump(nueva_data, otro_json, indent=4)

    with open('edwin_json.json', 'r') as otro_json:
        json_data = json.load(otro_json)

    print('Mostrar el contenido del archivo mi_json')
    print(json.dumps(json_data, indent=4))
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()
    
    print("terminamos")