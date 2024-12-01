from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JEOODHEBJJP(_message.Message):
    __slots__ = ("NOLBCHIACJI", "LHFDNDCNAIO", "EJNINFFFKJP")
    NOLBCHIACJI_FIELD_NUMBER: _ClassVar[int]
    LHFDNDCNAIO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NOLBCHIACJI: _AvatarInfo_pb2.AvatarInfo
    LHFDNDCNAIO: _AvatarInfo_pb2.AvatarInfo
    EJNINFFFKJP: int
    def __init__(self, NOLBCHIACJI: _Optional[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]] = ..., LHFDNDCNAIO: _Optional[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
