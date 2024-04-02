from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, 
                url_clic: str, sub_tipo: str) -> None:
        self._ancho = ancho if ancho > 0 else 1
        self._alto = alto if alto > 0 else 1
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self._sub_tipo = sub_tipo
    
    @property
    def ancho(self):
        return self._ancho
    
    @property
    def alto(self):
        return self._alto
    
    @property
    def url_archivo(self):
        return self._url_archivo
    @ url_archivo.setter
    def url_archivo(self, nuevo_urlarchivo):
        self.url_archivo = nuevo_urlarchivo
    
    @property
    def url_clic(self):
        return self._url_clic
    @url_clic.setter
    def url_clic(self, nuevo_urlclick):
        self.url_clic = nuevo_urlclick
    
    @property
    def sub_tipo(self):
        return self._sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo: str):
        if nuevo_sub_tipo not in self.sub_Tipos:
            raise SubTipoInvalidoException(f"El subtipo '{nuevo_sub_tipo}' no es válido para este tipo de anuncio.")
        self._sub_tipo = nuevo_sub_tipo
    
    @staticmethod
    def mostrar_formatos():
        pass
    
    def comprimir_anuncio(self):
        pass
    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    formato = 'video'
    sub_Tipos = ['instream' , 'outstream']
    
    def __init__(self, url_archivo: str, url_clic: str, 
                sub_tipo: str, duracion: int) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion if duracion > 0 else 5
    
    def comprimir_anuncio(self):
        return 'COMPRESION DE VIDEO NO IMPLMENTADA AUN'
    def redimensionar_anuncio(self):
        return 'RECORTE DE VIDEO NO IMPLEMENTADO AUN'
    
    @staticmethod
    def mostrar_formatos():
        print("FORMATO Socia:")
        print("==========")
        for subtipo in Video.SUB_TIPOS:
            print(f"- {subtipo}")

class Display(Anuncio):
    formato = 'Display'
    sub_Tipos = ['tradicional' , 'native']
    
    def comprimir_anuncio(self):
        return 'COMPRESION DE ANUNCIOS DISPLAY NO IMPLEMENTADA AUN'
    def redimensionar_anuncio(self):
        return 'REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AUN'
    
    @staticmethod
    def mostrar_formatos():
        print("FORMATO Socia:")
        print("==========")
        for subtipo in Display.SUB_TIPOS:
            print(f"- {subtipo}")

class Social(Anuncio):
    formato = 'social'
    sub_Tipos = ['facebook' , 'linkedin']
    
    def comprimir_anuncio(self):
        return 'COMPRESION DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AUN'
    def redimensionar_anuncio(self):
        return 'REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLMENTADO AUN'
    
    @staticmethod
    def mostrar_formatos():
        print("FORMATO Socia:")
        print("==========")
        for subtipo in Social.SUB_TIPOS:
            print(f"- {subtipo}")