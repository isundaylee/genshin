from genshin.packet.proto import WidgetSlotTag_pb2 as _WidgetSlotTag_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetSlotData(_message.Message):
    __slots__ = ("tag", "material_id", "cd_over_time", "is_active")
    TAG_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CD_OVER_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    tag: _WidgetSlotTag_pb2.WidgetSlotTag
    material_id: int
    cd_over_time: int
    is_active: bool
    def __init__(self, tag: _Optional[_Union[_WidgetSlotTag_pb2.WidgetSlotTag, str]] = ..., material_id: _Optional[int] = ..., cd_over_time: _Optional[int] = ..., is_active: bool = ...) -> None: ...
