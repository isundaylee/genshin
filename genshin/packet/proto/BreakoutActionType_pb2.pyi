from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BREAKOUT_ACTION_TYPE_ACTION_TYPE_NONE: _ClassVar[BreakoutActionType]
    BREAKOUT_ACTION_TYPE_ACTION_TYPE_LAUNCH_BALL: _ClassVar[BreakoutActionType]
    BREAKOUT_ACTION_TYPE_ACTION_TYPE_DESTROY_BALL: _ClassVar[BreakoutActionType]
    BREAKOUT_ACTION_TYPE_ACTION_TYPE_FALLING_OBJECT: _ClassVar[BreakoutActionType]
    BREAKOUT_ACTION_TYPE_ACTION_TYPE_MISSILE: _ClassVar[BreakoutActionType]
BREAKOUT_ACTION_TYPE_ACTION_TYPE_NONE: BreakoutActionType
BREAKOUT_ACTION_TYPE_ACTION_TYPE_LAUNCH_BALL: BreakoutActionType
BREAKOUT_ACTION_TYPE_ACTION_TYPE_DESTROY_BALL: BreakoutActionType
BREAKOUT_ACTION_TYPE_ACTION_TYPE_FALLING_OBJECT: BreakoutActionType
BREAKOUT_ACTION_TYPE_ACTION_TYPE_MISSILE: BreakoutActionType
