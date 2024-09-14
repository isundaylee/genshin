from genshin.packet.proto import ChatInfo_pb2 as _ChatInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PullRecentChatRsp(_message.Message):
    __slots__ = ("retcode", "chat_info")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_INFO_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    chat_info: _containers.RepeatedCompositeFieldContainer[_ChatInfo_pb2.ChatInfo]
    def __init__(self, retcode: _Optional[int] = ..., chat_info: _Optional[_Iterable[_Union[_ChatInfo_pb2.ChatInfo, _Mapping]]] = ...) -> None: ...
