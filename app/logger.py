import logging
import os

LEVEL = os.getenv('LOG_LEVEL','INFO').upper()
logging.basicConfig(level=LEVEL, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger('autonomy')
