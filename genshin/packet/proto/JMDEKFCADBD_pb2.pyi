from genshin.packet.proto import FJCOKOHBJIN_pb2 as _FJCOKOHBJIN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JMDEKFCADBD(_message.Message):
    __slots__ = ("OMKGPFGKFNB", "BCKBKIDDFCD", "EEKFELFANGN", "NMCGOCIKDMO")
    OMKGPFGKFNB_FIELD_NUMBER: _ClassVar[int]
    BCKBKIDDFCD_FIELD_NUMBER: _ClassVar[int]
    EEKFELFANGN_FIELD_NUMBER: _ClassVar[int]
    NMCGOCIKDMO_FIELD_NUMBER: _ClassVar[int]
    OMKGPFGKFNB: _containers.RepeatedScalarFieldContainer[int]
    BCKBKIDDFCD: _containers.RepeatedCompositeFieldContainer[_FJCOKOHBJIN_pb2.FJCOKOHBJIN]
    EEKFELFANGN: _containers.RepeatedScalarFieldContainer[int]
    NMCGOCIKDMO: bool
    def __init__(self, OMKGPFGKFNB: _Optional[_Iterable[int]] = ..., BCKBKIDDFCD: _Optional[_Iterable[_Union[_FJCOKOHBJIN_pb2.FJCOKOHBJIN, _Mapping]]] = ..., EEKFELFANGN: _Optional[_Iterable[int]] = ..., NMCGOCIKDMO: bool = ...) -> None: ...
