import json
# Inicio herarquia de clases Logger
class Logger:
    """ Intarface Logger."""
    def log(self, msg: str) -> None:
        pass

class FileLogger(Logger):
    """ Clase que hereda de la interface Logger
        e implementa el metodo logger escribiendo en archivo plano."""
    def log(self, msg: str):
        file = open("log.txt","w")
        file.write(msg+"\n")
        file.close()

class ConsoleLogger(Logger):
    """ Clase que hereda de la interface Logger
        e implementa el metodo logger escribiendo en consola."""
    def log(self, msg: str) -> None:
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
def main():
    factory = LoggerFactory()
    logger = factory.getLogger()
    logger.log("A Message to Log")  
main()