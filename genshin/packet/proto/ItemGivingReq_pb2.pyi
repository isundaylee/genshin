from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemGivingReq(_message.Message):
    __slots__ = ("item_param_list", "giving_id", "item_guid_count_map")
    class ItemGuidCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ITEM_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    GIVING_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_GUID_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    item_param_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    giving_id: int
    item_guid_count_map: _containers.ScalarMap[int, int]
    def __init__(self, item_param_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., giving_id: _Optional[int] = ..., item_guid_count_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
