from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LEMFLBNJKGF(_message.Message):
    __slots__ = ("DAAKPCOABEP", "IHGJLFCGFIN", "EJNINFFFKJP", "HPCPNMECHGA")
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    IHGJLFCGFIN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    HPCPNMECHGA_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    IHGJLFCGFIN: int
    EJNINFFFKJP: int
    HPCPNMECHGA: bool
    def __init__(self, DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ..., IHGJLFCGFIN: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., HPCPNMECHGA: bool = ...) -> None: ...