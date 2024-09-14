from genshin.packet.proto import AddNoGachaAvatarCardTransferItem_pb2 as _AddNoGachaAvatarCardTransferItem_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddNoGachaAvatarCardNotify(_message.Message):
    __slots__ = ("initial_level", "avatar_id", "reason", "is_transfer_to_item", "item_id", "transfer_item_list", "initial_promote_level")
    INITIAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFER_TO_ITEM_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    INITIAL_PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    initial_level: int
    avatar_id: int
    reason: int
    is_transfer_to_item: bool
    item_id: int
    transfer_item_list: _containers.RepeatedCompositeFieldContainer[_AddNoGachaAvatarCardTransferItem_pb2.AddNoGachaAvatarCardTransferItem]
    initial_promote_level: int
    def __init__(self, initial_level: _Optional[int] = ..., avatar_id: _Optional[int] = ..., reason: _Optional[int] = ..., is_transfer_to_item: bool = ..., item_id: _Optional[int] = ..., transfer_item_list: _Optional[_Iterable[_Union[_AddNoGachaAvatarCardTransferItem_pb2.AddNoGachaAvatarCardTransferItem, _Mapping]]] = ..., initial_promote_level: _Optional[int] = ...) -> None: ...
