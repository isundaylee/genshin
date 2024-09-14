from genshin.packet.proto import ForgeQueueData_pb2 as _ForgeQueueData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeGetQueueDataRsp(_message.Message):
    __slots__ = ("max_queue_num", "retcode", "forge_queue_map")
    class ForgeQueueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _ForgeQueueData_pb2.ForgeQueueData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_ForgeQueueData_pb2.ForgeQueueData, _Mapping]] = ...) -> None: ...
    MAX_QUEUE_NUM_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    FORGE_QUEUE_MAP_FIELD_NUMBER: _ClassVar[int]
    max_queue_num: int
    retcode: int
    forge_queue_map: _containers.MessageMap[int, _ForgeQueueData_pb2.ForgeQueueData]
    def __init__(self, max_queue_num: _Optional[int] = ..., retcode: _Optional[int] = ..., forge_queue_map: _Optional[_Mapping[int, _ForgeQueueData_pb2.ForgeQueueData]] = ...) -> None: ...
