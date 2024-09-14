from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLimitedShopInfo(_message.Message):
    __slots__ = ("uid", "djinn_rot", "next_guest_open_time", "djinn_pos", "next_close_time", "next_open_time")
    UID_FIELD_NUMBER: _ClassVar[int]
    DJINN_ROT_FIELD_NUMBER: _ClassVar[int]
    NEXT_GUEST_OPEN_TIME_FIELD_NUMBER: _ClassVar[int]
    DJINN_POS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_OPEN_TIME_FIELD_NUMBER: _ClassVar[int]
    uid: int
    djinn_rot: _Vector_pb2.Vector
    next_guest_open_time: int
    djinn_pos: _Vector_pb2.Vector
    next_close_time: int
    next_open_time: int
    def __init__(self, uid: _Optional[int] = ..., djinn_rot: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., next_guest_open_time: _Optional[int] = ..., djinn_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., next_close_time: _Optional[int] = ..., next_open_time: _Optional[int] = ...) -> None: ...
