from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTER_TYPE_NONE: _ClassVar[EnterType]
    ENTER_TYPE_SELF: _ClassVar[EnterType]
    ENTER_TYPE_GOTO: _ClassVar[EnterType]
    ENTER_TYPE_JUMP: _ClassVar[EnterType]
    ENTER_TYPE_OTHER: _ClassVar[EnterType]
    ENTER_TYPE_BACK: _ClassVar[EnterType]
    ENTER_TYPE_DUNGEON: _ClassVar[EnterType]
    ENTER_TYPE_DUNGEON_REPLAY: _ClassVar[EnterType]
    ENTER_TYPE_GOTO_BY_PORTAL: _ClassVar[EnterType]
    ENTER_TYPE_SELF_HOME: _ClassVar[EnterType]
    ENTER_TYPE_OTHER_HOME: _ClassVar[EnterType]
    ENTER_TYPE_GOTO_RECREATE: _ClassVar[EnterType]
    ENTER_TYPE_GOTO_BY_TPL: _ClassVar[EnterType]
ENTER_TYPE_NONE: EnterType
ENTER_TYPE_SELF: EnterType
ENTER_TYPE_GOTO: EnterType
ENTER_TYPE_JUMP: EnterType
ENTER_TYPE_OTHER: EnterType
ENTER_TYPE_BACK: EnterType
ENTER_TYPE_DUNGEON: EnterType
ENTER_TYPE_DUNGEON_REPLAY: EnterType
ENTER_TYPE_GOTO_BY_PORTAL: EnterType
ENTER_TYPE_SELF_HOME: EnterType
ENTER_TYPE_OTHER_HOME: EnterType
ENTER_TYPE_GOTO_RECREATE: EnterType
ENTER_TYPE_GOTO_BY_TPL: EnterType
