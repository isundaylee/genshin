from genshin.packet.proto import ParentQuestRandomInfo_pb2 as _ParentQuestRandomInfo_pb2
from genshin.packet.proto import ChildQuest_pb2 as _ChildQuest_pb2
from genshin.packet.proto import InferencePageInfo_pb2 as _InferencePageInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParentQuest(_message.Message):
    __slots__ = ("random_info", "child_quest_list", "quest_var_seq", "parent_quest_state", "is_random", "MGIJFMCBJKE", "accept_time", "inference_page_list", "parent_quest_id", "CKJMKGOKNED", "is_finished", "time_var_map", "quest_var", "video_key")
    class TimeVarMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    RANDOM_INFO_FIELD_NUMBER: _ClassVar[int]
    CHILD_QUEST_LIST_FIELD_NUMBER: _ClassVar[int]
    QUEST_VAR_SEQ_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    MGIJFMCBJKE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_TIME_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_PAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    PARENT_QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CKJMKGOKNED_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    TIME_VAR_MAP_FIELD_NUMBER: _ClassVar[int]
    QUEST_VAR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_KEY_FIELD_NUMBER: _ClassVar[int]
    random_info: _ParentQuestRandomInfo_pb2.ParentQuestRandomInfo
    child_quest_list: _containers.RepeatedCompositeFieldContainer[_ChildQuest_pb2.ChildQuest]
    quest_var_seq: int
    parent_quest_state: int
    is_random: bool
    MGIJFMCBJKE: bool
    accept_time: int
    inference_page_list: _containers.RepeatedCompositeFieldContainer[_InferencePageInfo_pb2.InferencePageInfo]
    parent_quest_id: int
    CKJMKGOKNED: bool
    is_finished: bool
    time_var_map: _containers.ScalarMap[int, int]
    quest_var: _containers.RepeatedScalarFieldContainer[int]
    video_key: int
    def __init__(self, random_info: _Optional[_Union[_ParentQuestRandomInfo_pb2.ParentQuestRandomInfo, _Mapping]] = ..., child_quest_list: _Optional[_Iterable[_Union[_ChildQuest_pb2.ChildQuest, _Mapping]]] = ..., quest_var_seq: _Optional[int] = ..., parent_quest_state: _Optional[int] = ..., is_random: bool = ..., MGIJFMCBJKE: bool = ..., accept_time: _Optional[int] = ..., inference_page_list: _Optional[_Iterable[_Union[_InferencePageInfo_pb2.InferencePageInfo, _Mapping]]] = ..., parent_quest_id: _Optional[int] = ..., CKJMKGOKNED: bool = ..., is_finished: bool = ..., time_var_map: _Optional[_Mapping[int, int]] = ..., quest_var: _Optional[_Iterable[int]] = ..., video_key: _Optional[int] = ...) -> None: ...
