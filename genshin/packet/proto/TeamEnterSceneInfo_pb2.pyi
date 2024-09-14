from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from genshin.packet.proto import AbilityControlBlock_pb2 as _AbilityControlBlock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamEnterSceneInfo(_message.Message):
    __slots__ = ("team_entity_id", "team_ability_info", "ability_control_block")
    TEAM_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    ABILITY_CONTROL_BLOCK_FIELD_NUMBER: _ClassVar[int]
    team_entity_id: int
    team_ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    ability_control_block: _AbilityControlBlock_pb2.AbilityControlBlock
    def __init__(self, team_entity_id: _Optional[int] = ..., team_ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., ability_control_block: _Optional[_Union[_AbilityControlBlock_pb2.AbilityControlBlock, _Mapping]] = ...) -> None: ...
