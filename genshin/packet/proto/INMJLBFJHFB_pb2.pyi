from genshin.packet.proto import OMAKEENDNNC_pb2 as _OMAKEENDNNC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class INMJLBFJHFB(_message.Message):
    __slots__ = ("DIAODCECNOE", "NIHFNLLBLFG")
    DIAODCECNOE_FIELD_NUMBER: _ClassVar[int]
    NIHFNLLBLFG_FIELD_NUMBER: _ClassVar[int]
    DIAODCECNOE: _containers.RepeatedCompositeFieldContainer[_OMAKEENDNNC_pb2.OMAKEENDNNC]
    NIHFNLLBLFG: bool
    def __init__(self, DIAODCECNOE: _Optional[_Iterable[_Union[_OMAKEENDNNC_pb2.OMAKEENDNNC, _Mapping]]] = ..., NIHFNLLBLFG: bool = ...) -> None: ...
