import asyncio
# Beginning of Logger hierarchy
class Logger:
    """ Intarface Logger."""
    def log(self, msg: str) -> None:
        pass

class FileLogger(Logger):
    _instance = None
    """ Clase que hereda de la interface Logger
        e implementa el metodo logger escribiendo en archivo plano.
        
        Usa singleton para no crear mas instancias de la clase
        y usa locks para disminurir riesgo de concurrencia al escribir en archivo"""
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("nuevo")
            file = open("log.txt","w+")
            file.close()
        return(cls._instance)
    def __init__(self):
        self.lock = asyncio.Lock()
    async def log(self, msg: str):
        async with self.lock:
            file = open("log.txt","a")
            file.write(msg)
            file.close()        

class ConsoleLogger(Logger):
    """ Clase que hereda de la interface Logger
        e implementa el metodo logger escribiendo en consola.
        
        Fue requerido agregarle asincronismo para poder continuar funcionando como fabrica,
        ya que el FileLogger requiere asincronismo para escribir en fichero"""
    async def log(self, msg: str) -> None:
        lock = asyncio.Lock()
        async with lock:
            print(msg)

# End of Logger hierarchy