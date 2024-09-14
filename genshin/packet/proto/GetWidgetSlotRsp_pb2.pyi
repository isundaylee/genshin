from genshin.packet.proto import WidgetSlotData_pb2 as _WidgetSlotData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWidgetSlotRsp(_message.Message):
    __slots__ = ("retcode", "slot_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SLOT_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    slot_list: _containers.RepeatedCompositeFieldContainer[_WidgetSlotData_pb2.WidgetSlotData]
    def __init__(self, retcode: _Optional[int] = ..., slot_list: _Optional[_Iterable[_Union[_WidgetSlotData_pb2.WidgetSlotData, _Mapping]]] = ...) -> None: ...
