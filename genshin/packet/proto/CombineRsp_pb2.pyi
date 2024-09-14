from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CombineRsp(_message.Message):
    __slots__ = ("combine_id", "combine_count", "totalExtraItemList", "total_return_item_list", "totalRandomItemList", "avatar_guid", "retcode", "result_item_list", "cost_item_list")
    COMBINE_ID_FIELD_NUMBER: _ClassVar[int]
    COMBINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTALEXTRAITEMLIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RETURN_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTALRANDOMITEMLIST_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    RESULT_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    COST_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    combine_id: int
    combine_count: int
    totalExtraItemList: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    total_return_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    totalRandomItemList: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    avatar_guid: int
    retcode: int
    result_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    cost_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    def __init__(self, combine_id: _Optional[int] = ..., combine_count: _Optional[int] = ..., totalExtraItemList: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., total_return_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., totalRandomItemList: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., avatar_guid: _Optional[int] = ..., retcode: _Optional[int] = ..., result_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., cost_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ...) -> None: ...
