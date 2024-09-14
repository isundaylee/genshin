from genshin.packet.proto import MusicGameRecord_pb2 as _MusicGameRecord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MusicGameActivityDetailInfo(_message.Message):
    __slots__ = ("music_game_record_map",)
    class MusicGameRecordMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MusicGameRecord_pb2.MusicGameRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MusicGameRecord_pb2.MusicGameRecord, _Mapping]] = ...) -> None: ...
    MUSIC_GAME_RECORD_MAP_FIELD_NUMBER: _ClassVar[int]
    music_game_record_map: _containers.MessageMap[int, _MusicGameRecord_pb2.MusicGameRecord]
    def __init__(self, music_game_record_map: _Optional[_Mapping[int, _MusicGameRecord_pb2.MusicGameRecord]] = ...) -> None: ...
