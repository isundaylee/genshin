from genshin.packet.proto import IPKAAINFGNB_pb2 as _IPKAAINFGNB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HMLEGGBJCKF(_message.Message):
    __slots__ = ("EGAHDMMDKEH", "OEOHFONLEGA", "DNBEFLJLAMB", "HDGLGGBOOBH")
    EGAHDMMDKEH_FIELD_NUMBER: _ClassVar[int]
    OEOHFONLEGA_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    HDGLGGBOOBH_FIELD_NUMBER: _ClassVar[int]
    EGAHDMMDKEH: _containers.RepeatedCompositeFieldContainer[_IPKAAINFGNB_pb2.IPKAAINFGNB]
    OEOHFONLEGA: _containers.RepeatedScalarFieldContainer[int]
    DNBEFLJLAMB: int
    HDGLGGBOOBH: bool
    def __init__(self, EGAHDMMDKEH: _Optional[_Iterable[_Union[_IPKAAINFGNB_pb2.IPKAAINFGNB, _Mapping]]] = ..., OEOHFONLEGA: _Optional[_Iterable[int]] = ..., DNBEFLJLAMB: _Optional[int] = ..., HDGLGGBOOBH: bool = ...) -> None: ...
