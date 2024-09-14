from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetGadgetData(_message.Message):
    __slots__ = ("gadget_id", "gadget_entity_id_list")
    GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_ENTITY_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    gadget_id: int
    gadget_entity_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gadget_id: _Optional[int] = ..., gadget_entity_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
