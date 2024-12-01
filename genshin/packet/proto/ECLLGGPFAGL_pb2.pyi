from genshin.packet.proto import CCNNIDMJLJN_pb2 as _CCNNIDMJLJN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ECLLGGPFAGL(_message.Message):
    __slots__ = ("KIKEOBNGPPO", "JHNBPLFCBAJ")
    KIKEOBNGPPO_FIELD_NUMBER: _ClassVar[int]
    JHNBPLFCBAJ_FIELD_NUMBER: _ClassVar[int]
    KIKEOBNGPPO: _containers.RepeatedCompositeFieldContainer[_CCNNIDMJLJN_pb2.CCNNIDMJLJN]
    JHNBPLFCBAJ: bool
    def __init__(self, KIKEOBNGPPO: _Optional[_Iterable[_Union[_CCNNIDMJLJN_pb2.CCNNIDMJLJN, _Mapping]]] = ..., JHNBPLFCBAJ: bool = ...) -> None: ...
