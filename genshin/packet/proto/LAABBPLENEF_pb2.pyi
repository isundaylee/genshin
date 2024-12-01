from genshin.packet.proto import NKKKBOHMANL_pb2 as _NKKKBOHMANL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LAABBPLENEF(_message.Message):
    __slots__ = ("EJNINFFFKJP", "KEGOCIPPFIN", "KGCONLDGJPG", "GHLBJAHJEHF", "FPPFKJELHDO")
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    KEGOCIPPFIN_FIELD_NUMBER: _ClassVar[int]
    KGCONLDGJPG_FIELD_NUMBER: _ClassVar[int]
    GHLBJAHJEHF_FIELD_NUMBER: _ClassVar[int]
    FPPFKJELHDO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP: int
    KEGOCIPPFIN: int
    KGCONLDGJPG: _NKKKBOHMANL_pb2.NKKKBOHMANL
    GHLBJAHJEHF: int
    FPPFKJELHDO: int
    def __init__(self, EJNINFFFKJP: _Optional[int] = ..., KEGOCIPPFIN: _Optional[int] = ..., KGCONLDGJPG: _Optional[_Union[_NKKKBOHMANL_pb2.NKKKBOHMANL, str]] = ..., GHLBJAHJEHF: _Optional[int] = ..., FPPFKJELHDO: _Optional[int] = ...) -> None: ...
