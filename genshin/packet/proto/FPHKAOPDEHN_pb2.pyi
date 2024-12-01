from genshin.packet.proto import LINCBKJPOLL_pb2 as _LINCBKJPOLL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FPHKAOPDEHN(_message.Message):
    __slots__ = ("JCMCHGNNLMJ", "level", "FBDOBGJGNBF", "GGEMJKEMJPK")
    JCMCHGNNLMJ_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    FBDOBGJGNBF_FIELD_NUMBER: _ClassVar[int]
    GGEMJKEMJPK_FIELD_NUMBER: _ClassVar[int]
    JCMCHGNNLMJ: int
    level: int
    FBDOBGJGNBF: _LINCBKJPOLL_pb2.LINCBKJPOLL
    GGEMJKEMJPK: int
    def __init__(self, JCMCHGNNLMJ: _Optional[int] = ..., level: _Optional[int] = ..., FBDOBGJGNBF: _Optional[_Union[_LINCBKJPOLL_pb2.LINCBKJPOLL, str]] = ..., GGEMJKEMJPK: _Optional[int] = ...) -> None: ...
