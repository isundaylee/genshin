from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from genshin.packet.proto import AvatarExpeditionInfo_pb2 as _AvatarExpeditionInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarExpeditionGetRewardRsp(_message.Message):
    __slots__ = ("extra_item_list", "expedition_info_map", "retcode", "item_list")
    class ExpeditionInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_AvatarExpeditionInfo_pb2.AvatarExpeditionInfo, _Mapping]] = ...) -> None: ...
    EXTRA_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    EXPEDITION_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    extra_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    expedition_info_map: _containers.MessageMap[int, _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo]
    retcode: int
    item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    def __init__(self, extra_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., expedition_info_map: _Optional[_Mapping[int, _AvatarExpeditionInfo_pb2.AvatarExpeditionInfo]] = ..., retcode: _Optional[int] = ..., item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ...) -> None: ...
