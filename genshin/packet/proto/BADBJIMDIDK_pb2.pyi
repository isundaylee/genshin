from genshin.packet.proto import MLHHGNPCLGK_pb2 as _MLHHGNPCLGK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BADBJIMDIDK(_message.Message):
    __slots__ = ("FJAMCDJDJOA", "FCPECPMOGOJ", "OMENIAMEDCE", "IMIOGMDOKCB", "CCLBEPHGCEK")
    FJAMCDJDJOA_FIELD_NUMBER: _ClassVar[int]
    FCPECPMOGOJ_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    CCLBEPHGCEK_FIELD_NUMBER: _ClassVar[int]
    FJAMCDJDJOA: int
    FCPECPMOGOJ: int
    OMENIAMEDCE: bool
    IMIOGMDOKCB: _MLHHGNPCLGK_pb2.MLHHGNPCLGK
    CCLBEPHGCEK: int
    def __init__(self, FJAMCDJDJOA: _Optional[int] = ..., FCPECPMOGOJ: _Optional[int] = ..., OMENIAMEDCE: bool = ..., IMIOGMDOKCB: _Optional[_Union[_MLHHGNPCLGK_pb2.MLHHGNPCLGK, str]] = ..., CCLBEPHGCEK: _Optional[int] = ...) -> None: ...
