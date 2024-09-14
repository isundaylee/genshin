from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import ForwardType_pb2 as _ForwardType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtDoSkillSuccNotify(_message.Message):
    __slots__ = ("forward", "skill_id", "forward_type", "caster_id")
    FORWARD_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    CASTER_ID_FIELD_NUMBER: _ClassVar[int]
    forward: _Vector_pb2.Vector
    skill_id: int
    forward_type: _ForwardType_pb2.ForwardType
    caster_id: int
    def __init__(self, forward: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., skill_id: _Optional[int] = ..., forward_type: _Optional[_Union[_ForwardType_pb2.ForwardType, str]] = ..., caster_id: _Optional[int] = ...) -> None: ...
