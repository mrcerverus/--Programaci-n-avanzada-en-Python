from datetime import date
from campania import Campania
from error import LargoExcedidoException, SubTipoInvalidoException

# Crear una instancia de Campania con un anuncio de tipo Video
anuncio_video = {
    "tipo": "video",
    "url_archivo": "video.mp4",
    "url_clic": "https://ejemplo.com",
    "sub_tipo": "instream",
    "duracion": 10
}

try:
    campania = Campania("Campaña de ejemplo", date.today(), date.today(), 
                        [anuncio_video])
except LargoExcedidoException as e:
    with open('error.log', 'a') as f:
        f.write(f'LargoExcedidoException: {e}\n')

# Solicitar al usuario un nuevo nombre de campaña y un nuevo subtipo para el anuncio
try:
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    nuevo_sub_tipo = input("Ingrese el nuevo subtipo para el anuncio de video: ")
    
    campania.nombre = nuevo_nombre
    campania.anuncios[0].sub_tipo = nuevo_sub_tipo
    
except LargoExcedidoException as e:
    with open('error.log', 'a+') as f:
        f.write(f'LargoExcedidoException: {e}\n')
except SubTipoInvalidoException as e:
    with open('error.log', 'a+') as f:
        f.write(f'SubTipoInvalidoException: {e}\n')