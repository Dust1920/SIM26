
# Información Descargada.
raw_folder = "raw_data"

# Información formateada para su conversión a tidy
medium_folder = "medium_data"

# Información estilizada en muchos archivos. 
tidy_data = "tidy_data"

# Información estilizada y almacenada en pocos archivos. 
database_folder = 'databases'



# (Funcion) Descargar archivos mediante internet
import requests as r
def descarga(url, save_path, filename):
    html = r.get(url)
    with open(save_path + '\\' + filename) as download:
        download.write(r.content)


print('Bien Hecho')