from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GJBCMIGGHEM(_message.Message):
    __slots__ = ("EFCDELGMMKG", "PMFOIANCCED", "EJNINFFFKJP")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    PMFOIANCCED_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_AvatarInfo_pb2.AvatarInfo]
    PMFOIANCCED: int
    EJNINFFFKJP: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]]] = ..., PMFOIANCCED: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
