from genshin.packet.proto import PlayerDieType_pb2 as _PlayerDieType_pb2
from genshin.packet.proto import ServerBuff_pb2 as _ServerBuff_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeStateChangeNotify(_message.Message):
    __slots__ = ("attack_tag", "move_reliable_seq", "EPGOBHIEDOI", "entity_id", "life_state", "die_type", "server_buff_list", "source_entity_id")
    ATTACK_TAG_FIELD_NUMBER: _ClassVar[int]
    MOVE_RELIABLE_SEQ_FIELD_NUMBER: _ClassVar[int]
    EPGOBHIEDOI_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    DIE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_BUFF_LIST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    attack_tag: str
    move_reliable_seq: int
    EPGOBHIEDOI: _containers.RepeatedScalarFieldContainer[str]
    entity_id: int
    life_state: int
    die_type: _PlayerDieType_pb2.PlayerDieType
    server_buff_list: _containers.RepeatedCompositeFieldContainer[_ServerBuff_pb2.ServerBuff]
    source_entity_id: int
    def __init__(self, attack_tag: _Optional[str] = ..., move_reliable_seq: _Optional[int] = ..., EPGOBHIEDOI: _Optional[_Iterable[str]] = ..., entity_id: _Optional[int] = ..., life_state: _Optional[int] = ..., die_type: _Optional[_Union[_PlayerDieType_pb2.PlayerDieType, str]] = ..., server_buff_list: _Optional[_Iterable[_Union[_ServerBuff_pb2.ServerBuff, _Mapping]]] = ..., source_entity_id: _Optional[int] = ...) -> None: ...
