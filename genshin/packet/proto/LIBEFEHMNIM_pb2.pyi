from genshin.packet.proto import DHDEBBIPIIF_pb2 as _DHDEBBIPIIF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LIBEFEHMNIM(_message.Message):
    __slots__ = ("EJNINFFFKJP", "MPNJAOCKMAH", "CKEHABLGHNN", "FINAHGLFHAG", "JCHHJFLDLGA")
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    CKEHABLGHNN_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    JCHHJFLDLGA_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP: int
    MPNJAOCKMAH: int
    CKEHABLGHNN: _DHDEBBIPIIF_pb2.DHDEBBIPIIF
    FINAHGLFHAG: int
    JCHHJFLDLGA: bool
    def __init__(self, EJNINFFFKJP: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., CKEHABLGHNN: _Optional[_Union[_DHDEBBIPIIF_pb2.DHDEBBIPIIF, str]] = ..., FINAHGLFHAG: _Optional[int] = ..., JCHHJFLDLGA: bool = ...) -> None: ...
