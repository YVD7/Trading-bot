# example for testing cusmtom logger with color addition
from logger import CustomLogger

log = CustomLogger(__name__).get_logger()


data = []
for i in range(20):
    data.append(i)

print(data)
log.info(f"data print {data}")
log.debug("Data File")
log.critical("data inconveniance")