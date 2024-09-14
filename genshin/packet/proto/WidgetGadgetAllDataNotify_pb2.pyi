from genshin.packet.proto import WidgetGadgetData_pb2 as _WidgetGadgetData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetGadgetAllDataNotify(_message.Message):
    __slots__ = ("widget_gadget_data",)
    WIDGET_GADGET_DATA_FIELD_NUMBER: _ClassVar[int]
    widget_gadget_data: _containers.RepeatedCompositeFieldContainer[_WidgetGadgetData_pb2.WidgetGadgetData]
    def __init__(self, widget_gadget_data: _Optional[_Iterable[_Union[_WidgetGadgetData_pb2.WidgetGadgetData, _Mapping]]] = ...) -> None: ...
