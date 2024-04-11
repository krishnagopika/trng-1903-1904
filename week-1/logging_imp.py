import logging

logging.basicConfig(filename="sample.log", encoding='utf-8', filemode='w', level=logging.INFO)

logger = logging.getLogger(__name__)

for i in range(10):
    print(i)

logger.info("Prints numbers in range 10")

logger.error("An error occured")
