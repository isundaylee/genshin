from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtBulletDeactiveNotify(_message.Message):
    __slots__ = ("forward_type", "entity_id", "disappear_pos")
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DISAPPEAR_POS_FIELD_NUMBER: _ClassVar[int]
    forward_type: _ForwardType_pb2.ForwardType
    entity_id: int
    disappear_pos: _Vector_pb2.Vector
    def __init__(self, forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., entity_id: _Optional[int] = ..., disappear_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ...) -> None: ...
