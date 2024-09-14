from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePlayerSoundNotify(_message.Message):
    __slots__ = ("play_pos", "sound_name", "play_type")
    class PlaySoundType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAY_SOUND_NONE: _ClassVar[ScenePlayerSoundNotify.PlaySoundType]
        PLAY_SOUND_START: _ClassVar[ScenePlayerSoundNotify.PlaySoundType]
        PLAY_SOUND_STOP: _ClassVar[ScenePlayerSoundNotify.PlaySoundType]
    PLAY_SOUND_NONE: ScenePlayerSoundNotify.PlaySoundType
    PLAY_SOUND_START: ScenePlayerSoundNotify.PlaySoundType
    PLAY_SOUND_STOP: ScenePlayerSoundNotify.PlaySoundType
    PLAY_POS_FIELD_NUMBER: _ClassVar[int]
    SOUND_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    play_pos: _Vector_pb2.Vector
    sound_name: str
    play_type: ScenePlayerSoundNotify.PlaySoundType
    def __init__(self, play_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., sound_name: _Optional[str] = ..., play_type: _Optional[_Union[ScenePlayerSoundNotify.PlaySoundType, str]] = ...) -> None: ...
