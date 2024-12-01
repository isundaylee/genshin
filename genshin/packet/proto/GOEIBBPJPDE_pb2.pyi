from genshin.packet.proto import LKDGPHDKHLL_pb2 as _LKDGPHDKHLL_pb2
from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GOEIBBPJPDE(_message.Message):
    __slots__ = ("CBMEECGEBAK", "DCOFBPAIIMP", "CKDPFJPLBLJ", "EJNINFFFKJP")
    CBMEECGEBAK_FIELD_NUMBER: _ClassVar[int]
    DCOFBPAIIMP_FIELD_NUMBER: _ClassVar[int]
    CKDPFJPLBLJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    CBMEECGEBAK: _containers.RepeatedScalarFieldContainer[int]
    DCOFBPAIIMP: _containers.RepeatedCompositeFieldContainer[_LKDGPHDKHLL_pb2.LKDGPHDKHLL]
    CKDPFJPLBLJ: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    EJNINFFFKJP: int
    def __init__(self, CBMEECGEBAK: _Optional[_Iterable[int]] = ..., DCOFBPAIIMP: _Optional[_Iterable[_Union[_LKDGPHDKHLL_pb2.LKDGPHDKHLL, _Mapping]]] = ..., CKDPFJPLBLJ: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
