"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import re
import pandas as pd

espacios = r' {1,}'

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    
    with open('files/input/clusters_report.txt', 'r') as file:
        datos = []
        fila_actual = []
        for i, line in enumerate(file):
            line = line.strip()
            if line.startswith('---') or i in (0,1,2,3):
                continue
            
            # Linea vacia
            if line.strip() == '':
                datos.append(fila_actual)
                fila_actual = []
                continue

            separados_por_espacios = re.split(espacios, line)
            
            if separados_por_espacios[0].isnumeric():
                fila_actual = [separados_por_espacios[0], separados_por_espacios[1], separados_por_espacios[2], separados_por_espacios[4:]]
            else:
                fila_actual[3].extend(separados_por_espacios)

    datos_limpios = []

    for cluster, cantidad, porcentaje, palabras in datos:
        palabras = ' '.join(palabras)
        datos_limpios.append([int(cluster), int(cantidad), float(porcentaje.replace(',', '.') ), palabras.replace('.', '')])
    
    df = pd.DataFrame(datos_limpios, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    return df

