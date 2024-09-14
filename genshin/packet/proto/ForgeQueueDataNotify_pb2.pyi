from genshin.packet.proto import ForgeQueueData_pb2 as _ForgeQueueData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForgeQueueDataNotify(_message.Message):
    __slots__ = ("forge_queue_map", "removed_forge_queue_list")
    class ForgeQueueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _ForgeQueueData_pb2.ForgeQueueData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_ForgeQueueData_pb2.ForgeQueueData, _Mapping]] = ...) -> None: ...
    FORGE_QUEUE_MAP_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FORGE_QUEUE_LIST_FIELD_NUMBER: _ClassVar[int]
    forge_queue_map: _containers.MessageMap[int, _ForgeQueueData_pb2.ForgeQueueData]
    removed_forge_queue_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, forge_queue_map: _Optional[_Mapping[int, _ForgeQueueData_pb2.ForgeQueueData]] = ..., removed_forge_queue_list: _Optional[_Iterable[int]] = ...) -> None: ...
