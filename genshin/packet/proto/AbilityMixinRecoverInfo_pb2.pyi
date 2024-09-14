from genshin.packet.proto import MassivePropSyncInfo_pb2 as _MassivePropSyncInfo_pb2
from genshin.packet.proto import BreakoutSnapShot_pb2 as _BreakoutSnapShot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbilityMixinRecoverInfo(_message.Message):
    __slots__ = ("local_id", "data_list", "is_serverbuff_modifier", "massive_prop_list", "breakout_snap_shot", "instanced_ability_id", "instanced_modifier_id")
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_SERVERBUFF_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    MASSIVE_PROP_LIST_FIELD_NUMBER: _ClassVar[int]
    BREAKOUT_SNAP_SHOT_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_ABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCED_MODIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    local_id: int
    data_list: _containers.RepeatedScalarFieldContainer[int]
    is_serverbuff_modifier: bool
    massive_prop_list: _containers.RepeatedCompositeFieldContainer[_MassivePropSyncInfo_pb2.MassivePropSyncInfo]
    breakout_snap_shot: _BreakoutSnapShot_pb2.BreakoutSnapShot
    instanced_ability_id: int
    instanced_modifier_id: int
    def __init__(self, local_id: _Optional[int] = ..., data_list: _Optional[_Iterable[int]] = ..., is_serverbuff_modifier: bool = ..., massive_prop_list: _Optional[_Iterable[_Union[_MassivePropSyncInfo_pb2.MassivePropSyncInfo, _Mapping]]] = ..., breakout_snap_shot: _Optional[_Union[_BreakoutSnapShot_pb2.BreakoutSnapShot, _Mapping]] = ..., instanced_ability_id: _Optional[int] = ..., instanced_modifier_id: _Optional[int] = ...) -> None: ...
