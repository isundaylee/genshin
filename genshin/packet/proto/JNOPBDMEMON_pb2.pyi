from genshin.packet.proto import JMHIPEJJPKG_pb2 as _JMHIPEJJPKG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JNOPBDMEMON(_message.Message):
    __slots__ = ("ILKGEFDHPFI", "ENELDMCHONK", "avatar_id")
    ILKGEFDHPFI_FIELD_NUMBER: _ClassVar[int]
    ENELDMCHONK_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    ILKGEFDHPFI: _containers.RepeatedScalarFieldContainer[int]
    ENELDMCHONK: _containers.RepeatedCompositeFieldContainer[_JMHIPEJJPKG_pb2.JMHIPEJJPKG]
    avatar_id: int
    def __init__(self, ILKGEFDHPFI: _Optional[_Iterable[int]] = ..., ENELDMCHONK: _Optional[_Iterable[_Union[_JMHIPEJJPKG_pb2.JMHIPEJJPKG, _Mapping]]] = ..., avatar_id: _Optional[int] = ...) -> None: ...
