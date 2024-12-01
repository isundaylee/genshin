from genshin.packet.proto import KOGANDHHOCG_pb2 as _KOGANDHHOCG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FEMBHMJOEGM(_message.Message):
    __slots__ = ("KABODNMEGEK", "GHDCFEHNMNO", "KICINEKPPJO")
    KABODNMEGEK_FIELD_NUMBER: _ClassVar[int]
    GHDCFEHNMNO_FIELD_NUMBER: _ClassVar[int]
    KICINEKPPJO_FIELD_NUMBER: _ClassVar[int]
    KABODNMEGEK: _containers.RepeatedCompositeFieldContainer[_KOGANDHHOCG_pb2.KOGANDHHOCG]
    GHDCFEHNMNO: int
    KICINEKPPJO: int
    def __init__(self, KABODNMEGEK: _Optional[_Iterable[_Union[_KOGANDHHOCG_pb2.KOGANDHHOCG, _Mapping]]] = ..., GHDCFEHNMNO: _Optional[int] = ..., KICINEKPPJO: _Optional[int] = ...) -> None: ...
