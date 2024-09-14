from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneFishInfo(_message.Message):
    __slots__ = ("fish_id", "fish_pool_entity_id", "fish_pool_pos", "fish_pool_gadget_id", "last_shock_time")
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    FISH_POOL_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FISH_POOL_POS_FIELD_NUMBER: _ClassVar[int]
    FISH_POOL_GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SHOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    fish_pool_entity_id: int
    fish_pool_pos: _Vector_pb2.Vector
    fish_pool_gadget_id: int
    last_shock_time: int
    def __init__(self, fish_id: _Optional[int] = ..., fish_pool_entity_id: _Optional[int] = ..., fish_pool_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., fish_pool_gadget_id: _Optional[int] = ..., last_shock_time: _Optional[int] = ...) -> None: ...
