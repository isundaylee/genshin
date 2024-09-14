from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayTeamEntityInfo(_message.Message):
    __slots__ = ("entity_id", "player_uid", "authority_peer_id", "gadget_config_id", "ability_info")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_UID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    GADGET_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    player_uid: int
    authority_peer_id: int
    gadget_config_id: int
    ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    def __init__(self, entity_id: _Optional[int] = ..., player_uid: _Optional[int] = ..., authority_peer_id: _Optional[int] = ..., gadget_config_id: _Optional[int] = ..., ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ...) -> None: ...
