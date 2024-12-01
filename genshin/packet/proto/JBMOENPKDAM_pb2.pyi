from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JBMOENPKDAM(_message.Message):
    __slots__ = ("CKDPFJPLBLJ", "KEOOJGFGMLH", "CBMEECGEBAK", "CHDOOKBIKLM", "DNBEFLJLAMB", "FINAHGLFHAG")
    CKDPFJPLBLJ_FIELD_NUMBER: _ClassVar[int]
    KEOOJGFGMLH_FIELD_NUMBER: _ClassVar[int]
    CBMEECGEBAK_FIELD_NUMBER: _ClassVar[int]
    CHDOOKBIKLM_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    CKDPFJPLBLJ: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    KEOOJGFGMLH: _containers.RepeatedScalarFieldContainer[int]
    CBMEECGEBAK: _containers.RepeatedScalarFieldContainer[int]
    CHDOOKBIKLM: _containers.RepeatedScalarFieldContainer[int]
    DNBEFLJLAMB: int
    FINAHGLFHAG: int
    def __init__(self, CKDPFJPLBLJ: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., KEOOJGFGMLH: _Optional[_Iterable[int]] = ..., CBMEECGEBAK: _Optional[_Iterable[int]] = ..., CHDOOKBIKLM: _Optional[_Iterable[int]] = ..., DNBEFLJLAMB: _Optional[int] = ..., FINAHGLFHAG: _Optional[int] = ...) -> None: ...
