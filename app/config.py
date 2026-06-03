from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

CURRENT_FILE = DATA_DIR / "current_devices.json"

NEW_FILE = DATA_DIR / "new_device.json"

LOGGER = Path(__file__).resolve().parent.parent

LOGGER_DIR = LOGGER / 'app'
LOGGER_DIR = LOGGER_DIR / 'loggs.txt'


