from genshin.packet.proto import AMJCDJNJKOI_pb2 as _AMJCDJNJKOI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GKEGLHBKJPL(_message.Message):
    __slots__ = ("NIJOKNFDDIO", "PNDPNMBDOKF", "OODHONBEHCH")
    NIJOKNFDDIO_FIELD_NUMBER: _ClassVar[int]
    PNDPNMBDOKF_FIELD_NUMBER: _ClassVar[int]
    OODHONBEHCH_FIELD_NUMBER: _ClassVar[int]
    NIJOKNFDDIO: _containers.RepeatedScalarFieldContainer[int]
    PNDPNMBDOKF: _containers.RepeatedCompositeFieldContainer[_AMJCDJNJKOI_pb2.AMJCDJNJKOI]
    OODHONBEHCH: int
    def __init__(self, NIJOKNFDDIO: _Optional[_Iterable[int]] = ..., PNDPNMBDOKF: _Optional[_Iterable[_Union[_AMJCDJNJKOI_pb2.AMJCDJNJKOI, _Mapping]]] = ..., OODHONBEHCH: _Optional[int] = ...) -> None: ...
