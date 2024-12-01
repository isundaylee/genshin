from genshin.packet.proto import EOCGCFPPLOE_pb2 as _EOCGCFPPLOE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FKJOHKKAOPO(_message.Message):
    __slots__ = ("EMLFLNAKIAI", "PGADBOLPFFA", "MBBKAENBCKD")
    EMLFLNAKIAI_FIELD_NUMBER: _ClassVar[int]
    PGADBOLPFFA_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    EMLFLNAKIAI: _containers.RepeatedCompositeFieldContainer[_EOCGCFPPLOE_pb2.EOCGCFPPLOE]
    PGADBOLPFFA: int
    MBBKAENBCKD: int
    def __init__(self, EMLFLNAKIAI: _Optional[_Iterable[_Union[_EOCGCFPPLOE_pb2.EOCGCFPPLOE, _Mapping]]] = ..., PGADBOLPFFA: _Optional[int] = ..., MBBKAENBCKD: _Optional[int] = ...) -> None: ...
