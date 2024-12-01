from genshin.packet.proto import PEIJAJNGGOE_pb2 as _PEIJAJNGGOE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HDCFBPPBPLF(_message.Message):
    __slots__ = ("avatar_list",)
    AVATAR_LIST_FIELD_NUMBER: _ClassVar[int]
    avatar_list: _containers.RepeatedCompositeFieldContainer[_PEIJAJNGGOE_pb2.PEIJAJNGGOE]
    def __init__(self, avatar_list: _Optional[_Iterable[_Union[_PEIJAJNGGOE_pb2.PEIJAJNGGOE, _Mapping]]] = ...) -> None: ...
