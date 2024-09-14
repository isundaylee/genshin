from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetSorushInfo(_message.Message):
    __slots__ = ("slot", "rot", "pos", "MHMHPPJKAHM", "JMOJHHHKHEL", "EOFNCKAMIKB")
    SLOT_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MHMHPPJKAHM_FIELD_NUMBER: _ClassVar[int]
    JMOJHHHKHEL_FIELD_NUMBER: _ClassVar[int]
    EOFNCKAMIKB_FIELD_NUMBER: _ClassVar[int]
    slot: int
    rot: _Vector_pb2.Vector
    pos: _Vector_pb2.Vector
    MHMHPPJKAHM: bool
    JMOJHHHKHEL: bool
    EOFNCKAMIKB: bool
    def __init__(self, slot: _Optional[int] = ..., rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., MHMHPPJKAHM: bool = ..., JMOJHHHKHEL: bool = ..., EOFNCKAMIKB: bool = ...) -> None: ...
