import asyncio
from src.logger_factory import LoggerFactory


async def main():
    factory = LoggerFactory()
    logger = factory.getLogger()
    task1 = asyncio.create_task(logger.log("A Message to Log1")) 
    task2 = asyncio.create_task(logger.log("A Message to Log2"))
    task3 = asyncio.create_task(logger.log("A Message to Log3"))
    await task1
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(main())