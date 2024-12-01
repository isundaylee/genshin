from genshin.packet.proto import CEGMHFPBAJJ_pb2 as _CEGMHFPBAJJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FMAMOMMNHBL(_message.Message):
    __slots__ = ("IJGDEMJNFNN", "GGJJFNDHAPL", "NEHNEFODOGM", "HKKADANMJIE")
    IJGDEMJNFNN_FIELD_NUMBER: _ClassVar[int]
    GGJJFNDHAPL_FIELD_NUMBER: _ClassVar[int]
    NEHNEFODOGM_FIELD_NUMBER: _ClassVar[int]
    HKKADANMJIE_FIELD_NUMBER: _ClassVar[int]
    IJGDEMJNFNN: _containers.RepeatedCompositeFieldContainer[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ]
    GGJJFNDHAPL: int
    NEHNEFODOGM: bool
    HKKADANMJIE: int
    def __init__(self, IJGDEMJNFNN: _Optional[_Iterable[_Union[_CEGMHFPBAJJ_pb2.CEGMHFPBAJJ, _Mapping]]] = ..., GGJJFNDHAPL: _Optional[int] = ..., NEHNEFODOGM: bool = ..., HKKADANMJIE: _Optional[int] = ...) -> None: ...
