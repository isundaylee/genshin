from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtAvatarExitFocusNotify(_message.Message):
    __slots__ = ("finish_forward", "forward_type", "entity_id")
    FINISH_FORWARD_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    finish_forward: _Vector_pb2.Vector
    forward_type: _ForwardType_pb2.ForwardType
    entity_id: int
    def __init__(self, finish_forward: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., entity_id: _Optional[int] = ...) -> None: ...
