from genshin.packet.proto import JCJCMAIBCAO_pb2 as _JCJCMAIBCAO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EHDFPAFLHIL(_message.Message):
    __slots__ = ("IIKBLHJBCIO", "EJNINFFFKJP")
    IIKBLHJBCIO_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    IIKBLHJBCIO: _JCJCMAIBCAO_pb2.JCJCMAIBCAO
    EJNINFFFKJP: int
    def __init__(self, IIKBLHJBCIO: _Optional[_Union[_JCJCMAIBCAO_pb2.JCJCMAIBCAO, _Mapping]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
