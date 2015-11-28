from .message import MessageSet
from .struct import Struct
from .types import Int8, Int16, Int32, Int64, Bytes, String, Array, Schema


class ProduceRequest(Struct):
    API_KEY = 0
    API_VERSION = 0
    SCHEMA = Schema(
        ('required_acks', Int16),
        ('timeout', Int32),
        ('topics', Array(
            ('topic', String('utf-8')),
            ('partitions', Array(
                ('partition', Int32),
                ('messages', MessageSet)))))
    )


class ProduceResponse(Struct):
    API_KEY = 0
    API_VERSION = 0
    SCHEMA = Schema(
        ('topics', Array(
            ('topic', String('utf-8')),
            ('partitions', Array(
                ('partition', Int32),
                ('error_code', Int16),
                ('offset', Int64)))))
    )
