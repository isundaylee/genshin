from genshin.packet.proto import AvatarInfo_pb2 as _AvatarInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DBEPEJJIIAO(_message.Message):
    __slots__ = ("EFCDELGMMKG", "OGPMCPPLGIB", "EJNINFFFKJP")
    class OGPMCPPLGIBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    OGPMCPPLGIB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_AvatarInfo_pb2.AvatarInfo]
    OGPMCPPLGIB: _containers.ScalarMap[int, float]
    EJNINFFFKJP: int
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_AvatarInfo_pb2.AvatarInfo, _Mapping]]] = ..., OGPMCPPLGIB: _Optional[_Mapping[int, float]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
