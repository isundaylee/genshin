from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetSlotOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIDGET_SLOT_OP_ATTACH: _ClassVar[WidgetSlotOp]
    WIDGET_SLOT_OP_DETACH: _ClassVar[WidgetSlotOp]
WIDGET_SLOT_OP_ATTACH: WidgetSlotOp
WIDGET_SLOT_OP_DETACH: WidgetSlotOp
