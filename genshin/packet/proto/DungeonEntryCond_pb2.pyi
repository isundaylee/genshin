from genshin.packet.proto import DungeonEntryBlockReason_pb2 as _DungeonEntryBlockReason_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEntryCond(_message.Message):
    __slots__ = ("cond_reason", "param1")
    COND_REASON_FIELD_NUMBER: _ClassVar[int]
    PARAM1_FIELD_NUMBER: _ClassVar[int]
    cond_reason: _DungeonEntryBlockReason_pb2.DungeonEntryBlockReason
    param1: int
    def __init__(self, cond_reason: _Optional[_Union[_DungeonEntryBlockReason_pb2.DungeonEntryBlockReason, str]] = ..., param1: _Optional[int] = ...) -> None: ...
