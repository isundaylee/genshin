from genshin.packet.proto import FHPEAIOOGCI_pb2 as _FHPEAIOOGCI_pb2
from genshin.packet.proto import OEFKBIFAPLF_pb2 as _OEFKBIFAPLF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BJLDHBEPNNI(_message.Message):
    __slots__ = ("CBPCBPAHCEN", "JIFOCCKIFKB")
    CBPCBPAHCEN_FIELD_NUMBER: _ClassVar[int]
    JIFOCCKIFKB_FIELD_NUMBER: _ClassVar[int]
    CBPCBPAHCEN: _containers.RepeatedCompositeFieldContainer[_FHPEAIOOGCI_pb2.FHPEAIOOGCI]
    JIFOCCKIFKB: _OEFKBIFAPLF_pb2.OEFKBIFAPLF
    def __init__(self, CBPCBPAHCEN: _Optional[_Iterable[_Union[_FHPEAIOOGCI_pb2.FHPEAIOOGCI, _Mapping]]] = ..., JIFOCCKIFKB: _Optional[_Union[_OEFKBIFAPLF_pb2.OEFKBIFAPLF, str]] = ...) -> None: ...
