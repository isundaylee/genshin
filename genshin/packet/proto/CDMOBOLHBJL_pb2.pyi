from genshin.packet.proto import GNDPPDJEIHI_pb2 as _GNDPPDJEIHI_pb2
from genshin.packet.proto import IPDFPEJJFJL_pb2 as _IPDFPEJJFJL_pb2
from genshin.packet.proto import OAMHDLMDFKP_pb2 as _OAMHDLMDFKP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDMOBOLHBJL(_message.Message):
    __slots__ = ("BCLBHOBHBIM", "BFAFICCJAAA", "OCCDLHPHNIH")
    BCLBHOBHBIM_FIELD_NUMBER: _ClassVar[int]
    BFAFICCJAAA_FIELD_NUMBER: _ClassVar[int]
    OCCDLHPHNIH_FIELD_NUMBER: _ClassVar[int]
    BCLBHOBHBIM: _GNDPPDJEIHI_pb2.GNDPPDJEIHI
    BFAFICCJAAA: _IPDFPEJJFJL_pb2.IPDFPEJJFJL
    OCCDLHPHNIH: _OAMHDLMDFKP_pb2.OAMHDLMDFKP
    def __init__(self, BCLBHOBHBIM: _Optional[_Union[_GNDPPDJEIHI_pb2.GNDPPDJEIHI, _Mapping]] = ..., BFAFICCJAAA: _Optional[_Union[_IPDFPEJJFJL_pb2.IPDFPEJJFJL, _Mapping]] = ..., OCCDLHPHNIH: _Optional[_Union[_OAMHDLMDFKP_pb2.OAMHDLMDFKP, _Mapping]] = ...) -> None: ...
