from genshin.packet.proto import NPJPIOOLOKO_pb2 as _NPJPIOOLOKO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FCFJDPGCOMN(_message.Message):
    __slots__ = ("GNBHBGOILFP", "HNMJKBEPNML", "ANHDIMEGDLN")
    GNBHBGOILFP_FIELD_NUMBER: _ClassVar[int]
    HNMJKBEPNML_FIELD_NUMBER: _ClassVar[int]
    ANHDIMEGDLN_FIELD_NUMBER: _ClassVar[int]
    GNBHBGOILFP: _containers.RepeatedCompositeFieldContainer[_NPJPIOOLOKO_pb2.NPJPIOOLOKO]
    HNMJKBEPNML: int
    ANHDIMEGDLN: int
    def __init__(self, GNBHBGOILFP: _Optional[_Iterable[_Union[_NPJPIOOLOKO_pb2.NPJPIOOLOKO, _Mapping]]] = ..., HNMJKBEPNML: _Optional[int] = ..., ANHDIMEGDLN: _Optional[int] = ...) -> None: ...
