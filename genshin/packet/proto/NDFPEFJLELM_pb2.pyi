from genshin.packet.proto import IHFCIFDKMPA_pb2 as _IHFCIFDKMPA_pb2
from genshin.packet.proto import CIIMAOJPKCK_pb2 as _CIIMAOJPKCK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NDFPEFJLELM(_message.Message):
    __slots__ = ("CPALNCBBDEC", "KCKEPCMLIHI", "MPFLDFDOGAI", "NMIKCMLKNDM")
    CPALNCBBDEC_FIELD_NUMBER: _ClassVar[int]
    KCKEPCMLIHI_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    CPALNCBBDEC: _containers.RepeatedCompositeFieldContainer[_IHFCIFDKMPA_pb2.IHFCIFDKMPA]
    KCKEPCMLIHI: _containers.RepeatedCompositeFieldContainer[_CIIMAOJPKCK_pb2.CIIMAOJPKCK]
    MPFLDFDOGAI: bool
    NMIKCMLKNDM: int
    def __init__(self, CPALNCBBDEC: _Optional[_Iterable[_Union[_IHFCIFDKMPA_pb2.IHFCIFDKMPA, _Mapping]]] = ..., KCKEPCMLIHI: _Optional[_Iterable[_Union[_CIIMAOJPKCK_pb2.CIIMAOJPKCK, _Mapping]]] = ..., MPFLDFDOGAI: bool = ..., NMIKCMLKNDM: _Optional[int] = ...) -> None: ...
