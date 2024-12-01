from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from genshin.packet.proto import CKLEEGMPDGN_pb2 as _CKLEEGMPDGN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HMLLBOPJCJI(_message.Message):
    __slots__ = ("NNPMLGAPAAN", "GBCMDOPCLIK", "AGMHMDHEFKD")
    NNPMLGAPAAN_FIELD_NUMBER: _ClassVar[int]
    GBCMDOPCLIK_FIELD_NUMBER: _ClassVar[int]
    AGMHMDHEFKD_FIELD_NUMBER: _ClassVar[int]
    NNPMLGAPAAN: _OLHEKLKENDN_pb2.OLHEKLKENDN
    GBCMDOPCLIK: int
    AGMHMDHEFKD: _CKLEEGMPDGN_pb2.CKLEEGMPDGN
    def __init__(self, NNPMLGAPAAN: _Optional[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]] = ..., GBCMDOPCLIK: _Optional[int] = ..., AGMHMDHEFKD: _Optional[_Union[_CKLEEGMPDGN_pb2.CKLEEGMPDGN, str]] = ...) -> None: ...
