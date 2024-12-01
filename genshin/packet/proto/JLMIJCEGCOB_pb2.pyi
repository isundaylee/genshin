from genshin.packet.proto import BGDCPBEGANK_pb2 as _BGDCPBEGANK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JLMIJCEGCOB(_message.Message):
    __slots__ = ("NEFMGJIDAAK", "MPNJAOCKMAH", "LDIILMAHHNG")
    NEFMGJIDAAK_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    LDIILMAHHNG_FIELD_NUMBER: _ClassVar[int]
    NEFMGJIDAAK: _containers.RepeatedCompositeFieldContainer[_BGDCPBEGANK_pb2.BGDCPBEGANK]
    MPNJAOCKMAH: int
    LDIILMAHHNG: int
    def __init__(self, NEFMGJIDAAK: _Optional[_Iterable[_Union[_BGDCPBEGANK_pb2.BGDCPBEGANK, _Mapping]]] = ..., MPNJAOCKMAH: _Optional[int] = ..., LDIILMAHHNG: _Optional[int] = ...) -> None: ...
