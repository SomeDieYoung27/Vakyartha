from itertools import islice
from typing import Optional

import numpy as np
import openai
import tiktoken
from tenacity import (
    retry,
    retry_if_not_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)
from theflow.utils.modules import import_dotted_string

from kotaemon.base import Param

from .base import BaseEmbeddings, Document, DocumentWithEmbedding

