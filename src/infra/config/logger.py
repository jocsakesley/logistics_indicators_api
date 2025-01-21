

import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format='{"app": "%(name)s", "level": "%(levelname)s", "message": "%(message)s", "file": "%(filename)s", "line": "%(lineno)d"}',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)