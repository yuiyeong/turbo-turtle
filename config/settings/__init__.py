import os

from dotenv import load_dotenv

load_dotenv()


if os.getenv("DEBUG") == "True":
    from .dev import *
else:
    from .base import *
