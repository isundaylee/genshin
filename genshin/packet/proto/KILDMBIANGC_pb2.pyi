from genshin.packet.proto import BGPAHBMKBAG_pb2 as _BGPAHBMKBAG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KILDMBIANGC(_message.Message):
    __slots__ = ("IFIPFMLJPGC", "EJNINFFFKJP")
    IFIPFMLJPGC_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    IFIPFMLJPGC: _containers.RepeatedCompositeFieldContainer[_BGPAHBMKBAG_pb2.BGPAHBMKBAG]
    EJNINFFFKJP: int
    def __init__(self, IFIPFMLJPGC: _Optional[_Iterable[_Union[_BGPAHBMKBAG_pb2.BGPAHBMKBAG, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
