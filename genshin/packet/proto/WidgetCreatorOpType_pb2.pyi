from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetCreatorOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIDGET_CREATOR_TYPE_NONE: _ClassVar[WidgetCreatorOpType]
    WIDGET_CREATOR_TYPE_RETRACT: _ClassVar[WidgetCreatorOpType]
    WIDGET_CREATOR_TYPE_RETRACT_AND_CREATE: _ClassVar[WidgetCreatorOpType]
WIDGET_CREATOR_TYPE_NONE: WidgetCreatorOpType
WIDGET_CREATOR_TYPE_RETRACT: WidgetCreatorOpType
WIDGET_CREATOR_TYPE_RETRACT_AND_CREATE: WidgetCreatorOpType
