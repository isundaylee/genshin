from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IKFLBJKKNHI(_message.Message):
    __slots__ = ("FLBIAPLPJIA", "EDNEEOBKGEJ", "LHHGPMOKLKG", "NDJMHDAMKHI")
    FLBIAPLPJIA_FIELD_NUMBER: _ClassVar[int]
    EDNEEOBKGEJ_FIELD_NUMBER: _ClassVar[int]
    LHHGPMOKLKG_FIELD_NUMBER: _ClassVar[int]
    NDJMHDAMKHI_FIELD_NUMBER: _ClassVar[int]
    FLBIAPLPJIA: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    EDNEEOBKGEJ: int
    LHHGPMOKLKG: int
    NDJMHDAMKHI: bool
    def __init__(self, FLBIAPLPJIA: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., EDNEEOBKGEJ: _Optional[int] = ..., LHHGPMOKLKG: _Optional[int] = ..., NDJMHDAMKHI: bool = ...) -> None: ...
