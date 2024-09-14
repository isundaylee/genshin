from genshin.packet.proto import BreakoutPhysicalObject_pb2 as _BreakoutPhysicalObject_pb2
from genshin.packet.proto import BreakoutAction_pb2 as _BreakoutAction_pb2
from genshin.packet.proto import BreakoutSpawnPoint_pb2 as _BreakoutSpawnPoint_pb2
from genshin.packet.proto import BreakoutElementReactionCounter_pb2 as _BreakoutElementReactionCounter_pb2
from genshin.packet.proto import BreakoutSyncConnectUidInfo_pb2 as _BreakoutSyncConnectUidInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutSnapShot(_message.Message):
    __slots__ = ("client_game_time", "server_game_time", "ball_list", "physical_object_list", "action_list", "wave_index", "is_finish", "score", "combo", "max_combo", "life_count", "wave_suite_index", "spawn_point_list", "remaining_boss_hp", "brick_element_reaction_list", "ball_element_reaction_list", "uid_info_list", "dynamic_object_list", "id_index_list", "raw_client_game_time")
    CLIENT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    BALL_LIST_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    WAVE_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_FINISH_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    COMBO_FIELD_NUMBER: _ClassVar[int]
    MAX_COMBO_FIELD_NUMBER: _ClassVar[int]
    LIFE_COUNT_FIELD_NUMBER: _ClassVar[int]
    WAVE_SUITE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SPAWN_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    REMAINING_BOSS_HP_FIELD_NUMBER: _ClassVar[int]
    BRICK_ELEMENT_REACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    BALL_ELEMENT_REACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    UID_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    ID_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    RAW_CLIENT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    client_game_time: int
    server_game_time: int
    ball_list: _containers.RepeatedCompositeFieldContainer[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject]
    physical_object_list: _containers.RepeatedCompositeFieldContainer[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject]
    action_list: _containers.RepeatedCompositeFieldContainer[_BreakoutAction_pb2.BreakoutAction]
    wave_index: int
    is_finish: bool
    score: int
    combo: int
    max_combo: int
    life_count: int
    wave_suite_index: int
    spawn_point_list: _containers.RepeatedCompositeFieldContainer[_BreakoutSpawnPoint_pb2.BreakoutSpawnPoint]
    remaining_boss_hp: int
    brick_element_reaction_list: _containers.RepeatedCompositeFieldContainer[_BreakoutElementReactionCounter_pb2.BreakoutElementReactionCounter]
    ball_element_reaction_list: _containers.RepeatedCompositeFieldContainer[_BreakoutElementReactionCounter_pb2.BreakoutElementReactionCounter]
    uid_info_list: _containers.RepeatedCompositeFieldContainer[_BreakoutSyncConnectUidInfo_pb2.BreakoutSyncConnectUidInfo]
    dynamic_object_list: _containers.RepeatedCompositeFieldContainer[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject]
    id_index_list: _containers.RepeatedScalarFieldContainer[int]
    raw_client_game_time: int
    def __init__(self, client_game_time: _Optional[int] = ..., server_game_time: _Optional[int] = ..., ball_list: _Optional[_Iterable[_Union[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject, _Mapping]]] = ..., physical_object_list: _Optional[_Iterable[_Union[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject, _Mapping]]] = ..., action_list: _Optional[_Iterable[_Union[_BreakoutAction_pb2.BreakoutAction, _Mapping]]] = ..., wave_index: _Optional[int] = ..., is_finish: bool = ..., score: _Optional[int] = ..., combo: _Optional[int] = ..., max_combo: _Optional[int] = ..., life_count: _Optional[int] = ..., wave_suite_index: _Optional[int] = ..., spawn_point_list: _Optional[_Iterable[_Union[_BreakoutSpawnPoint_pb2.BreakoutSpawnPoint, _Mapping]]] = ..., remaining_boss_hp: _Optional[int] = ..., brick_element_reaction_list: _Optional[_Iterable[_Union[_BreakoutElementReactionCounter_pb2.BreakoutElementReactionCounter, _Mapping]]] = ..., ball_element_reaction_list: _Optional[_Iterable[_Union[_BreakoutElementReactionCounter_pb2.BreakoutElementReactionCounter, _Mapping]]] = ..., uid_info_list: _Optional[_Iterable[_Union[_BreakoutSyncConnectUidInfo_pb2.BreakoutSyncConnectUidInfo, _Mapping]]] = ..., dynamic_object_list: _Optional[_Iterable[_Union[_BreakoutPhysicalObject_pb2.BreakoutPhysicalObject, _Mapping]]] = ..., id_index_list: _Optional[_Iterable[int]] = ..., raw_client_game_time: _Optional[int] = ...) -> None: ...
