from genshin.packet.proto import BDCDECGDJGF_pb2 as _BDCDECGDJGF_pb2
from genshin.packet.proto import CGPHGGDKIHF_pb2 as _CGPHGGDKIHF_pb2
from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HCGEKEDNIAE(_message.Message):
    __slots__ = ("OCMLKEOONKO", "JMOODLIKPLI", "FJIAEMGLAGI", "DNBEFLJLAMB", "DAAKPCOABEP", "IHGJLFCGFIN")
    OCMLKEOONKO_FIELD_NUMBER: _ClassVar[int]
    JMOODLIKPLI_FIELD_NUMBER: _ClassVar[int]
    FJIAEMGLAGI_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    IHGJLFCGFIN_FIELD_NUMBER: _ClassVar[int]
    OCMLKEOONKO: _BDCDECGDJGF_pb2.BDCDECGDJGF
    JMOODLIKPLI: bool
    FJIAEMGLAGI: _CGPHGGDKIHF_pb2.CGPHGGDKIHF
    DNBEFLJLAMB: int
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    IHGJLFCGFIN: int
    def __init__(self, OCMLKEOONKO: _Optional[_Union[_BDCDECGDJGF_pb2.BDCDECGDJGF, str]] = ..., JMOODLIKPLI: bool = ..., FJIAEMGLAGI: _Optional[_Union[_CGPHGGDKIHF_pb2.CGPHGGDKIHF, str]] = ..., DNBEFLJLAMB: _Optional[int] = ..., DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ..., IHGJLFCGFIN: _Optional[int] = ...) -> None: ...
