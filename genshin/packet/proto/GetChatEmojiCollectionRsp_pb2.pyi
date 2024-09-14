from genshin.packet.proto import ChatEmojiCollectionData_pb2 as _ChatEmojiCollectionData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetChatEmojiCollectionRsp(_message.Message):
    __slots__ = ("chat_emoji_collection_data", "retcode")
    CHAT_EMOJI_COLLECTION_DATA_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    chat_emoji_collection_data: _ChatEmojiCollectionData_pb2.ChatEmojiCollectionData
    retcode: int
    def __init__(self, chat_emoji_collection_data: _Optional[_Union[_ChatEmojiCollectionData_pb2.ChatEmojiCollectionData, _Mapping]] = ..., retcode: _Optional[int] = ...) -> None: ...
