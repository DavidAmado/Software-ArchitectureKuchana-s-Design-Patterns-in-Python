from src.logger_factory import LoggerFactory

if __name__ == "__main__":
    factory = LoggerFactory()
    logger = factory.getLogger()
    logger.log("A Message to Log")

