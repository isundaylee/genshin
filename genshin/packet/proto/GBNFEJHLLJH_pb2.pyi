from genshin.packet.proto import PIMEINBAJFB_pb2 as _PIMEINBAJFB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GBNFEJHLLJH(_message.Message):
    __slots__ = ("FIDFLABLFMO", "KPNBOHHNKHE", "CJOKFLDEFMB", "EJNINFFFKJP")
    FIDFLABLFMO_FIELD_NUMBER: _ClassVar[int]
    KPNBOHHNKHE_FIELD_NUMBER: _ClassVar[int]
    CJOKFLDEFMB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    FIDFLABLFMO: _containers.RepeatedScalarFieldContainer[int]
    KPNBOHHNKHE: _containers.RepeatedCompositeFieldContainer[_PIMEINBAJFB_pb2.PIMEINBAJFB]
    CJOKFLDEFMB: int
    EJNINFFFKJP: int
    def __init__(self, FIDFLABLFMO: _Optional[_Iterable[int]] = ..., KPNBOHHNKHE: _Optional[_Iterable[_Union[_PIMEINBAJFB_pb2.PIMEINBAJFB, _Mapping]]] = ..., CJOKFLDEFMB: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
