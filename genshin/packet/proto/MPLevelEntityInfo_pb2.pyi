from genshin.packet.proto import AbilitySyncStateInfo_pb2 as _AbilitySyncStateInfo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MPLevelEntityInfo(_message.Message):
    __slots__ = ("ability_info", "entity_id", "authority_peer_id")
    ABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    ability_info: _AbilitySyncStateInfo_pb2.AbilitySyncStateInfo
    entity_id: int
    authority_peer_id: int
    def __init__(self, ability_info: _Optional[_Union[_AbilitySyncStateInfo_pb2.AbilitySyncStateInfo, _Mapping]] = ..., entity_id: _Optional[int] = ..., authority_peer_id: _Optional[int] = ...) -> None: ...
