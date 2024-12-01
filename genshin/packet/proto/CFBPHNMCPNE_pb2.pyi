from genshin.packet.proto import JEKGEGJBGLF_pb2 as _JEKGEGJBGLF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CFBPHNMCPNE(_message.Message):
    __slots__ = ("EAIPGEMKNPO", "GLKNGDDNOCN", "HDNBCJCKKFL", "CCENFGCDLNP", "JABGACILLEC")
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    HDNBCJCKKFL_FIELD_NUMBER: _ClassVar[int]
    CCENFGCDLNP_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO: int
    GLKNGDDNOCN: bool
    HDNBCJCKKFL: _JEKGEGJBGLF_pb2.JEKGEGJBGLF
    CCENFGCDLNP: int
    JABGACILLEC: int
    def __init__(self, EAIPGEMKNPO: _Optional[int] = ..., GLKNGDDNOCN: bool = ..., HDNBCJCKKFL: _Optional[_Union[_JEKGEGJBGLF_pb2.JEKGEGJBGLF, str]] = ..., CCENFGCDLNP: _Optional[int] = ..., JABGACILLEC: _Optional[int] = ...) -> None: ...
