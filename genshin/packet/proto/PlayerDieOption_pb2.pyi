from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerDieOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIE_OPT_NONE: _ClassVar[PlayerDieOption]
    DIE_OPT_REPLAY: _ClassVar[PlayerDieOption]
    DIE_OPT_CANCEL: _ClassVar[PlayerDieOption]
    DIE_OPT_REVIVE: _ClassVar[PlayerDieOption]
DIE_OPT_NONE: PlayerDieOption
DIE_OPT_REPLAY: PlayerDieOption
DIE_OPT_CANCEL: PlayerDieOption
DIE_OPT_REVIVE: PlayerDieOption
