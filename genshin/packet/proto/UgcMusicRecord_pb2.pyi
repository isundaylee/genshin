from genshin.packet.proto import UgcMusicTrack_pb2 as _UgcMusicTrack_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UgcMusicRecord(_message.Message):
    __slots__ = ("music_track_list", "music_id")
    MUSIC_TRACK_LIST_FIELD_NUMBER: _ClassVar[int]
    MUSIC_ID_FIELD_NUMBER: _ClassVar[int]
    music_track_list: _containers.RepeatedCompositeFieldContainer[_UgcMusicTrack_pb2.UgcMusicTrack]
    music_id: int
    def __init__(self, music_track_list: _Optional[_Iterable[_Union[_UgcMusicTrack_pb2.UgcMusicTrack, _Mapping]]] = ..., music_id: _Optional[int] = ...) -> None: ...
