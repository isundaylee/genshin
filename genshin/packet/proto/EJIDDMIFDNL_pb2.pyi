from genshin.packet.proto import EICIMOKGOOK_pb2 as _EICIMOKGOOK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJIDDMIFDNL(_message.Message):
    __slots__ = ("OABGPLHCBFO", "MGDKAGGEOIO", "DNBEFLJLAMB", "COEBNIJNNNE")
    OABGPLHCBFO_FIELD_NUMBER: _ClassVar[int]
    MGDKAGGEOIO_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    COEBNIJNNNE_FIELD_NUMBER: _ClassVar[int]
    OABGPLHCBFO: _containers.RepeatedScalarFieldContainer[int]
    MGDKAGGEOIO: _containers.RepeatedCompositeFieldContainer[_EICIMOKGOOK_pb2.EICIMOKGOOK]
    DNBEFLJLAMB: int
    COEBNIJNNNE: int
    def __init__(self, OABGPLHCBFO: _Optional[_Iterable[int]] = ..., MGDKAGGEOIO: _Optional[_Iterable[_Union[_EICIMOKGOOK_pb2.EICIMOKGOOK, _Mapping]]] = ..., DNBEFLJLAMB: _Optional[int] = ..., COEBNIJNNNE: _Optional[int] = ...) -> None: ...
