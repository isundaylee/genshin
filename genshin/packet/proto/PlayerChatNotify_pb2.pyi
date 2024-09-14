from genshin.packet.proto import ChatInfo_pb2 as _ChatInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerChatNotify(_message.Message):
    __slots__ = ("channel_id", "chat_info")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_INFO_FIELD_NUMBER: _ClassVar[int]
    channel_id: int
    chat_info: _ChatInfo_pb2.ChatInfo
    def __init__(self, channel_id: _Optional[int] = ..., chat_info: _Optional[_Union[_ChatInfo_pb2.ChatInfo, _Mapping]] = ...) -> None: ...
