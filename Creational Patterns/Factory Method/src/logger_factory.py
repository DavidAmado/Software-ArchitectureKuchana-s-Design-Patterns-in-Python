import json
from src.logger_hierarchy import ConsoleLogger, FileLogger, Logger
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