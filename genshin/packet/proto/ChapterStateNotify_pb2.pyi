from genshin.packet.proto import ChapterState_pb2 as _ChapterState_pb2
from genshin.packet.proto import NeedPlayerLevel_pb2 as _NeedPlayerLevel_pb2
from genshin.packet.proto import NeedBeginTime_pb2 as _NeedBeginTime_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChapterStateNotify(_message.Message):
    __slots__ = ("chapter_id", "chapter_state", "need_player_level", "need_begin_time")
    CHAPTER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAPTER_STATE_FIELD_NUMBER: _ClassVar[int]
    NEED_PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NEED_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    chapter_id: int
    chapter_state: _ChapterState_pb2.ChapterState
    need_player_level: _NeedPlayerLevel_pb2.NeedPlayerLevel
    need_begin_time: _NeedBeginTime_pb2.NeedBeginTime
    def __init__(self, chapter_id: _Optional[int] = ..., chapter_state: _Optional[_Union[_ChapterState_pb2.ChapterState, str]] = ..., need_player_level: _Optional[_Union[_NeedPlayerLevel_pb2.NeedPlayerLevel, _Mapping]] = ..., need_begin_time: _Optional[_Union[_NeedBeginTime_pb2.NeedBeginTime, _Mapping]] = ...) -> None: ...
