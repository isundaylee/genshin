from genshin.packet.proto import PKNOABHFFKO_pb2 as _PKNOABHFFKO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BLFGKJCPJHO(_message.Message):
    __slots__ = ("JNCEPKPDICG", "IMLNHCHBMMD")
    JNCEPKPDICG_FIELD_NUMBER: _ClassVar[int]
    IMLNHCHBMMD_FIELD_NUMBER: _ClassVar[int]
    JNCEPKPDICG: _containers.RepeatedCompositeFieldContainer[_PKNOABHFFKO_pb2.PKNOABHFFKO]
    IMLNHCHBMMD: str
    def __init__(self, JNCEPKPDICG: _Optional[_Iterable[_Union[_PKNOABHFFKO_pb2.PKNOABHFFKO, _Mapping]]] = ..., IMLNHCHBMMD: _Optional[str] = ...) -> None: ...
