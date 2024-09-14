from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ModifierAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODIFIER_ACTION_ADDED: _ClassVar[ModifierAction]
    MODIFIER_ACTION_REMOVED: _ClassVar[ModifierAction]
MODIFIER_ACTION_ADDED: ModifierAction
MODIFIER_ACTION_REMOVED: ModifierAction
