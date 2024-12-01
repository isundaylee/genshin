from genshin.packet.proto import DHDEBBIPIIF_pb2 as _DHDEBBIPIIF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MFHGLBJEDKI(_message.Message):
    __slots__ = ("JFCKFGNOBBP", "CKEHABLGHNN", "EJNINFFFKJP", "FINAHGLFHAG", "MPNJAOCKMAH")
    JFCKFGNOBBP_FIELD_NUMBER: _ClassVar[int]
    CKEHABLGHNN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    JFCKFGNOBBP: str
    CKEHABLGHNN: _DHDEBBIPIIF_pb2.DHDEBBIPIIF
    EJNINFFFKJP: int
    FINAHGLFHAG: int
    MPNJAOCKMAH: int
    def __init__(self, JFCKFGNOBBP: _Optional[str] = ..., CKEHABLGHNN: _Optional[_Union[_DHDEBBIPIIF_pb2.DHDEBBIPIIF, str]] = ..., EJNINFFFKJP: _Optional[int] = ..., FINAHGLFHAG: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ...) -> None: ...
