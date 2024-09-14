from genshin.packet.proto import ItemHint_pb2 as _ItemHint_pb2
from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemAddHintNotify(_message.Message):
    __slots__ = ("item_list", "overflow_transformed_item_list", "is_transfered_from_avatar_card", "position", "reason", "is_position_valid", "is_general_reward_hiden", "quest_id")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    OVERFLOW_TRANSFORMED_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFERED_FROM_AVATAR_CARD_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_POSITION_VALID_FIELD_NUMBER: _ClassVar[int]
    IS_GENERAL_REWARD_HIDEN_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_ItemHint_pb2.ItemHint]
    overflow_transformed_item_list: _containers.RepeatedCompositeFieldContainer[_ItemHint_pb2.ItemHint]
    is_transfered_from_avatar_card: bool
    position: _Vector_pb2.Vector
    reason: int
    is_position_valid: bool
    is_general_reward_hiden: bool
    quest_id: int
    def __init__(self, item_list: _Optional[_Iterable[_Union[_ItemHint_pb2.ItemHint, _Mapping]]] = ..., overflow_transformed_item_list: _Optional[_Iterable[_Union[_ItemHint_pb2.ItemHint, _Mapping]]] = ..., is_transfered_from_avatar_card: bool = ..., position: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., reason: _Optional[int] = ..., is_position_valid: bool = ..., is_general_reward_hiden: bool = ..., quest_id: _Optional[int] = ...) -> None: ...
