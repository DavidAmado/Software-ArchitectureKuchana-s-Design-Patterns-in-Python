import json
import asyncio

# Inicio herarquia de clases Logger
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

# Fin herarquia de clases Logger

# Logger Factory
class LoggerFactory:
    def isFileLoggingEnabled(self):
        try:
            with open('./paremeters.json') as f:
                properties = json.load(f)
                print("properties",properties)
            if properties["FileLogging"].upper()=="ON":
                return (True)
        except:
            print("Excepcion con el archivo")
        return (False)
    def getLogger(self) -> Logger:
        if self.isFileLoggingEnabled():
            return(FileLogger())
        return(ConsoleLogger())
async def main():
    factory = LoggerFactory()
    logger = factory.getLogger()
    task1 = asyncio.create_task(logger.log("A Message to Log1\n")) 
    task2 = asyncio.create_task(logger.log("A Message to Log2\n"))
    task3 = asyncio.create_task(logger.log("A Message to Log3\n"))
    await task1
    await task2
    await task3

asyncio.run(main())