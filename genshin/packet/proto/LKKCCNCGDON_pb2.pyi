from genshin.packet.proto import OBJFDBHEAKJ_pb2 as _OBJFDBHEAKJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LKKCCNCGDON(_message.Message):
    __slots__ = ("DDPFMKJFPAK",)
    class DDPFMKJFPAKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _OBJFDBHEAKJ_pb2.OBJFDBHEAKJ
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_OBJFDBHEAKJ_pb2.OBJFDBHEAKJ, _Mapping]] = ...) -> None: ...
    DDPFMKJFPAK_FIELD_NUMBER: _ClassVar[int]
    DDPFMKJFPAK: _containers.MessageMap[int, _OBJFDBHEAKJ_pb2.OBJFDBHEAKJ]
    def __init__(self, DDPFMKJFPAK: _Optional[_Mapping[int, _OBJFDBHEAKJ_pb2.OBJFDBHEAKJ]] = ...) -> None: ...
