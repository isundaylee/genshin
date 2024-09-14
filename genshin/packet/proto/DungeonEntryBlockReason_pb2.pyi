from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEntryBlockReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUNGEON_ENTRY_REASON_NONE: _ClassVar[DungeonEntryBlockReason]
    DUNGEON_ENTRY_REASON_LEVEL: _ClassVar[DungeonEntryBlockReason]
    DUNGEON_ENTRY_REASON_QUEST: _ClassVar[DungeonEntryBlockReason]
    DUNGEON_ENTRY_REASON_MULIPLE: _ClassVar[DungeonEntryBlockReason]
DUNGEON_ENTRY_REASON_NONE: DungeonEntryBlockReason
DUNGEON_ENTRY_REASON_LEVEL: DungeonEntryBlockReason
DUNGEON_ENTRY_REASON_QUEST: DungeonEntryBlockReason
DUNGEON_ENTRY_REASON_MULIPLE: DungeonEntryBlockReason
