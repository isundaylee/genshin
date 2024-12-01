from genshin.packet.proto import MBIMHNFDGHN_pb2 as _MBIMHNFDGHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJKGCBAHDPB(_message.Message):
    __slots__ = ("BELACGKAHLM", "AGIDBEEINDE", "EPDMMGIMNCC")
    BELACGKAHLM_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    EPDMMGIMNCC_FIELD_NUMBER: _ClassVar[int]
    BELACGKAHLM: _MBIMHNFDGHN_pb2.MBIMHNFDGHN
    AGIDBEEINDE: int
    EPDMMGIMNCC: bool
    def __init__(self, BELACGKAHLM: _Optional[_Union[_MBIMHNFDGHN_pb2.MBIMHNFDGHN, str]] = ..., AGIDBEEINDE: _Optional[int] = ..., EPDMMGIMNCC: bool = ...) -> None: ...
