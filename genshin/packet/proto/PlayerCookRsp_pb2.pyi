from genshin.packet.proto import CookRecipeData_pb2 as _CookRecipeData_pb2
from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerCookRsp(_message.Message):
    __slots__ = ("retcode", "cook_count", "recipe_data", "qte_quality", "item_list", "extral_item_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    COOK_COUNT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_DATA_FIELD_NUMBER: _ClassVar[int]
    QTE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    EXTRAL_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    cook_count: int
    recipe_data: _CookRecipeData_pb2.CookRecipeData
    qte_quality: int
    item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    extral_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    def __init__(self, retcode: _Optional[int] = ..., cook_count: _Optional[int] = ..., recipe_data: _Optional[_Union[_CookRecipeData_pb2.CookRecipeData, _Mapping]] = ..., qte_quality: _Optional[int] = ..., item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., extral_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ...) -> None: ...
