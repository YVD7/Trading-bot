# setup
import subprocess
from logger import CustomLogger

log = CustomLogger(__name__).get_logger()

command = "pip install -r requirements.txt"
try:
    subprocess.check_call(command, shell=True)
    log.info(f"Successfully executed setup command: {command}")
except subprocess.CalledProcessError as e:
    log.error(f"Error executing command: {command}. Error: {e}")

