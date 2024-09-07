import psutil
from matchmaking.metric_type import MetricType
from matchmaking.config import MetricWeightsConfig

NUM_ITERATIONS = 100000

NUM_FIELDS = 3

PLAYER_NAMES = [
    "P01",
    "P2",
    "P3",
    "P4",
    "P5",
    "P6",
    "P7",
    "P8",
    "P9",
    "P10",
    "P11",
    "P12",
    "P13",
]

NUM_ROUNDS = len(PLAYER_NAMES)


METRIC_WEIGHTS_CONFIG = MetricWeightsConfig()


WORKERS = psutil.cpu_count()
