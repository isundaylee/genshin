from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GachaUpInfo(_message.Message):
    __slots__ = ("item_id_list", "item_parent_type")
    ITEM_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    item_id_list: _containers.RepeatedScalarFieldContainer[int]
    item_parent_type: int
    def __init__(self, item_id_list: _Optional[_Iterable[int]] = ..., item_parent_type: _Optional[int] = ...) -> None: ...
