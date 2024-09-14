from genshin.packet.proto import WidgetSlotOp_pb2 as _WidgetSlotOp_pb2
from genshin.packet.proto import WidgetSlotTag_pb2 as _WidgetSlotTag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetWidgetSlotRsp(_message.Message):
    __slots__ = ("retcode", "op", "material_id", "tag_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    op: _WidgetSlotOp_pb2.WidgetSlotOp
    material_id: int
    tag_list: _containers.RepeatedScalarFieldContainer[_WidgetSlotTag_pb2.WidgetSlotTag]
    def __init__(self, retcode: _Optional[int] = ..., op: _Optional[_Union[_WidgetSlotOp_pb2.WidgetSlotOp, str]] = ..., material_id: _Optional[int] = ..., tag_list: _Optional[_Iterable[_Union[_WidgetSlotTag_pb2.WidgetSlotTag, str]]] = ...) -> None: ...
