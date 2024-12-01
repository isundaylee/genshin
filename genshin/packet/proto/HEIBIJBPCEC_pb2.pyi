from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from genshin.packet.proto import BDCDECGDJGF_pb2 as _BDCDECGDJGF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HEIBIJBPCEC(_message.Message):
    __slots__ = ("IHGJLFCGFIN", "EJNINFFFKJP", "DAAKPCOABEP", "OCMLKEOONKO")
    IHGJLFCGFIN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    OCMLKEOONKO_FIELD_NUMBER: _ClassVar[int]
    IHGJLFCGFIN: int
    EJNINFFFKJP: int
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    OCMLKEOONKO: _BDCDECGDJGF_pb2.BDCDECGDJGF
    def __init__(self, IHGJLFCGFIN: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ..., OCMLKEOONKO: _Optional[_Union[_BDCDECGDJGF_pb2.BDCDECGDJGF, str]] = ...) -> None: ...
