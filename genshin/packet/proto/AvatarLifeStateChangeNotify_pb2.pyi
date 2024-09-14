from genshin.packet.proto import PlayerDieType_pb2 as _PlayerDieType_pb2
from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarLifeStateChangeNotify(_message.Message):
    __slots__ = ("source_entity_id", "EPGOBHIEDOI", "die_type", "avatar_guid", "move_reliable_seq", "life_state", "server_buff_list", "attack_tag")
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EPGOBHIEDOI_FIELD_NUMBER: _ClassVar[int]
    DIE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_GUID_FIELD_NUMBER: _ClassVar[int]
    MOVE_RELIABLE_SEQ_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    ATTACK_TAG_FIELD_NUMBER: _ClassVar[int]
    source_entity_id: int
    EPGOBHIEDOI: _containers.RepeatedScalarFieldContainer[str]
    die_type: _PlayerDieType_pb2.PlayerDieType
    avatar_guid: int
    move_reliable_seq: int
    life_state: int
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    attack_tag: str
    def __init__(self, source_entity_id: _Optional[int] = ..., EPGOBHIEDOI: _Optional[_Iterable[str]] = ..., die_type: _Optional[_Union[_PlayerDieType_pb2.PlayerDieType, str]] = ..., avatar_guid: _Optional[int] = ..., move_reliable_seq: _Optional[int] = ..., life_state: _Optional[int] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., attack_tag: _Optional[str] = ...) -> None: ...
