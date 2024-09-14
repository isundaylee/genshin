from genshin.packet.proto import BreakoutPhysicalObject_pb2 as _BreakoutPhysicalObject_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutSpawnPoint(_message.Message):
    __slots__ = ("id", "brick_suite_id", "spawned_brick_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAWNED_BRICK_LIST_FIELD_NUMBER: _ClassVar[int]
    id: int
    brick_suite_id: int
    spawned_brick_list: _containers.RepeatedCompositeFieldContainer[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject]
    def __init__(self, id: _Optional[int] = ..., brick_suite_id: _Optional[int] = ..., spawned_brick_list: _Optional[_Iterable[_Union[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject, _Mapping]]] = ...) -> None: ...
