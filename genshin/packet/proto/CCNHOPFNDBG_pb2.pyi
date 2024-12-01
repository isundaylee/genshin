from genshin.packet.proto import BAENJDFENNH_pb2 as _BAENJDFENNH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CCNHOPFNDBG(_message.Message):
    __slots__ = ("AMEHOKPOGLK", "ILGPAHIAHIG", "KKFHJLLLDEF", "EJNINFFFKJP", "NIOPJAGDBNM", "EIJPMMBMOHL")
    AMEHOKPOGLK_FIELD_NUMBER: _ClassVar[int]
    ILGPAHIAHIG_FIELD_NUMBER: _ClassVar[int]
    KKFHJLLLDEF_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    NIOPJAGDBNM_FIELD_NUMBER: _ClassVar[int]
    EIJPMMBMOHL_FIELD_NUMBER: _ClassVar[int]
    AMEHOKPOGLK: _containers.RepeatedCompositeFieldContainer[_BAENJDFENNH_pb2.BAENJDFENNH]
    ILGPAHIAHIG: bool
    KKFHJLLLDEF: bool
    EJNINFFFKJP: int
    NIOPJAGDBNM: int
    EIJPMMBMOHL: int
    def __init__(self, AMEHOKPOGLK: _Optional[_Iterable[_Union[_BAENJDFENNH_pb2.BAENJDFENNH, _Mapping]]] = ..., ILGPAHIAHIG: bool = ..., KKFHJLLLDEF: bool = ..., EJNINFFFKJP: _Optional[int] = ..., NIOPJAGDBNM: _Optional[int] = ..., EIJPMMBMOHL: _Optional[int] = ...) -> None: ...
