from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientGadgetInfo(_message.Message):
    __slots__ = ("camp_id", "camp_type", "guid", "owner_entity_id", "target_entity_id", "async_load", "is_peer_id_from_player", "target_entity_id_list", "target_lock_point_index_list")
    CAMP_ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ASYNC_LOAD_FIELD_NUMBER: _ClassVar[int]
    IS_PEER_ID_FROM_PLAYER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_LOCK_POINT_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    camp_id: int
    camp_type: int
    guid: int
    owner_entity_id: int
    target_entity_id: int
    async_load: bool
    is_peer_id_from_player: bool
    target_entity_id_list: _containers.RepeatedScalarFieldContainer[int]
    target_lock_point_index_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, camp_id: _Optional[int] = ..., camp_type: _Optional[int] = ..., guid: _Optional[int] = ..., owner_entity_id: _Optional[int] = ..., target_entity_id: _Optional[int] = ..., async_load: bool = ..., is_peer_id_from_player: bool = ..., target_entity_id_list: _Optional[_Iterable[int]] = ..., target_lock_point_index_list: _Optional[_Iterable[int]] = ...) -> None: ...
