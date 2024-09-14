from genshin.packet.proto import CoopPoint_pb2 as _CoopPoint_pb2
from genshin.packet.proto import CoopReward_pb2 as _CoopReward_pb2
from genshin.packet.proto import CoopCg_pb2 as _CoopCg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoopChapter(_message.Message):
    __slots__ = ("state", "LAAOIEBFJKP", "seen_ending_map", "coop_point_list", "coop_reward_list", "coop_cg_list", "id", "JDENGALMPJN", "EOMGDNCEACF", "HKOAKJNBIIO")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_CLOSE: _ClassVar[CoopChapter.State]
        STATE_COND_NOT_MEET: _ClassVar[CoopChapter.State]
        STATE_COND_MEET: _ClassVar[CoopChapter.State]
        STATE_ACCEPT: _ClassVar[CoopChapter.State]
    STATE_CLOSE: CoopChapter.State
    STATE_COND_NOT_MEET: CoopChapter.State
    STATE_COND_MEET: CoopChapter.State
    STATE_ACCEPT: CoopChapter.State
    class SeenEndingMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    LAAOIEBFJKP_FIELD_NUMBER: _ClassVar[int]
    SEEN_ENDING_MAP_FIELD_NUMBER: _ClassVar[int]
    COOP_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    COOP_REWARD_LIST_FIELD_NUMBER: _ClassVar[int]
    COOP_CG_LIST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JDENGALMPJN_FIELD_NUMBER: _ClassVar[int]
    EOMGDNCEACF_FIELD_NUMBER: _ClassVar[int]
    HKOAKJNBIIO_FIELD_NUMBER: _ClassVar[int]
    state: CoopChapter.State
    LAAOIEBFJKP: _containers.RepeatedScalarFieldContainer[int]
    seen_ending_map: _containers.ScalarMap[int, int]
    coop_point_list: _containers.RepeatedCompositeFieldContainer[_CoopPoint_pb2.CoopPoint]
    coop_reward_list: _containers.RepeatedCompositeFieldContainer[_CoopReward_pb2.CoopReward]
    coop_cg_list: _containers.RepeatedCompositeFieldContainer[_CoopCg_pb2.CoopCg]
    id: int
    JDENGALMPJN: int
    EOMGDNCEACF: _containers.RepeatedScalarFieldContainer[int]
    HKOAKJNBIIO: int
    def __init__(self, state: _Optional[_Union[CoopChapter.State, str]] = ..., LAAOIEBFJKP: _Optional[_Iterable[int]] = ..., seen_ending_map: _Optional[_Mapping[int, int]] = ..., coop_point_list: _Optional[_Iterable[_Union[_CoopPoint_pb2.CoopPoint, _Mapping]]] = ..., coop_reward_list: _Optional[_Iterable[_Union[_CoopReward_pb2.CoopReward, _Mapping]]] = ..., coop_cg_list: _Optional[_Iterable[_Union[_CoopCg_pb2.CoopCg, _Mapping]]] = ..., id: _Optional[int] = ..., JDENGALMPJN: _Optional[int] = ..., EOMGDNCEACF: _Optional[_Iterable[int]] = ..., HKOAKJNBIIO: _Optional[int] = ...) -> None: ...
