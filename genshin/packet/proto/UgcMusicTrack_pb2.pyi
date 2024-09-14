from genshin.packet.proto import UgcMusicNote_pb2 as _UgcMusicNote_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UgcMusicTrack(_message.Message):
    __slots__ = ("music_note_list",)
    MUSIC_NOTE_LIST_FIELD_NUMBER: _ClassVar[int]
    music_note_list: _containers.RepeatedCompositeFieldContainer[_UgcMusicNote_pb2.UgcMusicNote]
    def __init__(self, music_note_list: _Optional[_Iterable[_Union[_UgcMusicNote_pb2.UgcMusicNote, _Mapping]]] = ...) -> None: ...
