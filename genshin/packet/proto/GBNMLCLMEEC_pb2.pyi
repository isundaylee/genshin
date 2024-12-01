from genshin.packet.proto import CJEIMOKENAM_pb2 as _CJEIMOKENAM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GBNMLCLMEEC(_message.Message):
    __slots__ = ("PJMIHEEDBDB", "EJNINFFFKJP")
    PJMIHEEDBDB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    PJMIHEEDBDB: _containers.RepeatedCompositeFieldContainer[_CJEIMOKENAM_pb2.CJEIMOKENAM]
    EJNINFFFKJP: int
    def __init__(self, PJMIHEEDBDB: _Optional[_Iterable[_Union[_CJEIMOKENAM_pb2.CJEIMOKENAM, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
