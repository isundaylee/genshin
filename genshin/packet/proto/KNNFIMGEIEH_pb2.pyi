from genshin.packet.proto import GFIGAPGGLPI_pb2 as _GFIGAPGGLPI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KNNFIMGEIEH(_message.Message):
    __slots__ = ("HCLIEMDGGGC", "MPFLDFDOGAI", "EPPPBOLKBAC")
    HCLIEMDGGGC_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    EPPPBOLKBAC_FIELD_NUMBER: _ClassVar[int]
    HCLIEMDGGGC: _containers.RepeatedCompositeFieldContainer[_GFIGAPGGLPI_pb2.GFIGAPGGLPI]
    MPFLDFDOGAI: bool
    EPPPBOLKBAC: int
    def __init__(self, HCLIEMDGGGC: _Optional[_Iterable[_Union[_GFIGAPGGLPI_pb2.GFIGAPGGLPI, _Mapping]]] = ..., MPFLDFDOGAI: bool = ..., EPPPBOLKBAC: _Optional[int] = ...) -> None: ...
