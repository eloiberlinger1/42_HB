from .creatures import Flameling, Pyrodon, Aquabub, Torrential
from .factory_base import AbstractCreatureFactory
from .factory import (
    FireCreatureFactory,
    WaterCreatureFactory,
)

__all__ = [
    'Flameling',
    'Pyrodon',
    'Aquabub',
    'Torrential',
    'FireCreatureFactory',
    'WaterCreatureFactory',
    'AbstractCreatureFactory'
]

__version__ = "1.0.0"
__author__ = "Master Pythonicus"
