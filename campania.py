from datetime import date
from anuncio import Video, Display, Social
from error import LargoExcedidoException

class Campania:
    def __init__(self, nombre: str, fecha_inicio: date, 
                fecha_termino: date, anuncios) -> None:
        if len(nombre) >= 250:
            raise LargoExcedidoException('''
                El nombre de la campaña excede los 250 caracteres.
                ''')
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._fecha_termino = fecha_termino
        self.anuncios = [self._crear_anuncios(anuncio) for anuncio in anuncios]
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fechainicio):
        self.fecha_inicio = nueva_fechainicio
    
    @property      
    def fecha_termino(self):
        return self._fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, nueva_fechatermino):
        self.fecha_termino = nueva_fechatermino
        
    
    def _crear_anuncios(self,anuncio: dict):
        
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)
        
        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        elif tipo_anuncio == "display":
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)
    
    def _contar_anuncios(self):
        conteo = {'Video': 0, 'Display': 0, 'Social': 0}
        for anuncio in self._anuncios:
            if isinstance(anuncio, Video):
                conteo['Video'] += 1
            elif isinstance(anuncio, Display):
                conteo['Display'] += 1
            elif isinstance(anuncio, Social):
                conteo['Social'] += 1
        return f"{conteo['Video']} Video, {conteo['Display']} Display, {conteo['Social']} Social"
    
    def __str__(self) -> str:
        return f'''
            Nombre de la campaña: {self._nombre}
            Anuncios: {self._contar_anuncios()}
            '''