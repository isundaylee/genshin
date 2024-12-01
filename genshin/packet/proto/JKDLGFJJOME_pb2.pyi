from genshin.packet.proto import NGBDCGMNINN_pb2 as _NGBDCGMNINN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JKDLGFJJOME(_message.Message):
    __slots__ = ("MLOBACJPFEK", "OHNFAANFOBO", "LKMGMHHKKNB")
    MLOBACJPFEK_FIELD_NUMBER: _ClassVar[int]
    OHNFAANFOBO_FIELD_NUMBER: _ClassVar[int]
    LKMGMHHKKNB_FIELD_NUMBER: _ClassVar[int]
    MLOBACJPFEK: _containers.RepeatedCompositeFieldContainer[_NGBDCGMNINN_pb2.NGBDCGMNINN]
    OHNFAANFOBO: bool
    LKMGMHHKKNB: int
    def __init__(self, MLOBACJPFEK: _Optional[_Iterable[_Union[_NGBDCGMNINN_pb2.NGBDCGMNINN, _Mapping]]] = ..., OHNFAANFOBO: bool = ..., LKMGMHHKKNB: _Optional[int] = ...) -> None: ...
