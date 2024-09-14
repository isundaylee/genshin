from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DestroyMaterialRsp(_message.Message):
    __slots__ = ("item_count_list", "retcode", "item_id_list")
    ITEM_COUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    item_count_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    item_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, item_count_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ..., item_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
