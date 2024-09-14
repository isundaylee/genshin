from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CustomDungeonFinishType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOM_DUNGEON_FINISH_PLAY_NORMAL: _ClassVar[CustomDungeonFinishType]
    CUSTOM_DUNGEON_FINISH_PLAY_TRY: _ClassVar[CustomDungeonFinishType]
    CUSTOM_DUNGEON_FINISH_EDIT_TRY: _ClassVar[CustomDungeonFinishType]
    CUSTOM_DUNGEON_FINISH_SELF_PLAY_NORMAL: _ClassVar[CustomDungeonFinishType]
CUSTOM_DUNGEON_FINISH_PLAY_NORMAL: CustomDungeonFinishType
CUSTOM_DUNGEON_FINISH_PLAY_TRY: CustomDungeonFinishType
CUSTOM_DUNGEON_FINISH_EDIT_TRY: CustomDungeonFinishType
CUSTOM_DUNGEON_FINISH_SELF_PLAY_NORMAL: CustomDungeonFinishType
