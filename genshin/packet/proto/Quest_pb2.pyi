from genshin.packet.proto import LackingResourceInfo_pb2 as _LackingResourceInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Quest(_message.Message):
    __slots__ = ("quest_id", "state", "start_time", "is_random", "parent_quest_id", "quest_config_id", "start_game_time", "accept_time", "finish_progress_list", "fail_progress_list", "MLHFBAFCKIP", "EBPOIBHNPNH")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    START_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_PROGRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    FAIL_PROGRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    MLHFBAFCKIP_FIELD_NUMBER: _ClassVar[int]
    EBPOIBHNPNH_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    state: int
    start_time: int
    is_random: bool
    parent_quest_id: int
    quest_config_id: int
    start_game_time: int
    accept_time: int
    finish_progress_list: _containers.RepeatedScalarFieldContainer[int]
    fail_progress_list: _containers.RepeatedScalarFieldContainer[int]
    MLHFBAFCKIP: _containers.RepeatedScalarFieldContainer[int]
    EBPOIBHNPNH: _LackingResourceInfo_pb2.LackingResourceInfo
    def __init__(self, quest_id: _Optional[int] = ..., state: _Optional[int] = ..., start_time: _Optional[int] = ..., is_random: bool = ..., parent_quest_id: _Optional[int] = ..., quest_config_id: _Optional[int] = ..., start_game_time: _Optional[int] = ..., accept_time: _Optional[int] = ..., finish_progress_list: _Optional[_Iterable[int]] = ..., fail_progress_list: _Optional[_Iterable[int]] = ..., MLHFBAFCKIP: _Optional[_Iterable[int]] = ..., EBPOIBHNPNH: _Optional[_Union[_LackingResourceInfo_pb2.LackingResourceInfo, _Mapping]] = ...) -> None: ...
