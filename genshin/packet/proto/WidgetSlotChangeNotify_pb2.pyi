from genshin.packet.proto import WidgetSlotData_pb2 as _WidgetSlotData_pb2
from genshin.packet.proto import WidgetSlotOp_pb2 as _WidgetSlotOp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetSlotChangeNotify(_message.Message):
    __slots__ = ("slot", "op")
    SLOT_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    slot: _WidgetSlotData_pb2.WidgetSlotData
    op: _WidgetSlotOp_pb2.WidgetSlotOp
    def __init__(self, slot: _Optional[_Union[_WidgetSlotData_pb2.WidgetSlotData, _Mapping]] = ..., op: _Optional[_Union[_WidgetSlotOp_pb2.WidgetSlotOp, str]] = ...) -> None: ...
