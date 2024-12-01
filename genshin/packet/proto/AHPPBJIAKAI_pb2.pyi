from genshin.packet.proto import LGNOEBMGBOB_pb2 as _LGNOEBMGBOB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AHPPBJIAKAI(_message.Message):
    __slots__ = ("JPJLOCPLIHL",)
    class JPJLOCPLIHLEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _LGNOEBMGBOB_pb2.LGNOEBMGBOB
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_LGNOEBMGBOB_pb2.LGNOEBMGBOB, _Mapping]] = ...) -> None: ...
    JPJLOCPLIHL_FIELD_NUMBER: _ClassVar[int]
    JPJLOCPLIHL: _containers.MessageMap[int, _LGNOEBMGBOB_pb2.LGNOEBMGBOB]
    def __init__(self, JPJLOCPLIHL: _Optional[_Mapping[int, _LGNOEBMGBOB_pb2.LGNOEBMGBOB]] = ...) -> None: ...
