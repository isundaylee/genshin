from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OACNPIEBKHC(_message.Message):
    __slots__ = ("EJNINFFFKJP", "BPNKHEIFAHP", "DAAKPCOABEP", "IHGJLFCGFIN")
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    BPNKHEIFAHP_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    IHGJLFCGFIN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP: int
    BPNKHEIFAHP: bool
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    IHGJLFCGFIN: int
    def __init__(self, EJNINFFFKJP: _Optional[int] = ..., BPNKHEIFAHP: bool = ..., DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ..., IHGJLFCGFIN: _Optional[int] = ...) -> None: ...
