# Beginning of Logger hierarchy
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

# End Logger hierarchy