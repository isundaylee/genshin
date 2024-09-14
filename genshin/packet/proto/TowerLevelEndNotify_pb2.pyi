from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TowerLevelEndNotify(_message.Message):
    __slots__ = ("reward_item_list", "next_floor_id", "finished_star_cond_list", "continue_state", "is_success")
    class ContinueStateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTINUE_STATE_TYPE_CAN_NOT_CONTINUE: _ClassVar[TowerLevelEndNotify.ContinueStateType]
        CONTINUE_STATE_TYPE_CAN_ENTER_NEXT_LEVEL: _ClassVar[TowerLevelEndNotify.ContinueStateType]
        CONTINUE_STATE_TYPE_CAN_ENTER_NEXT_FLOOR: _ClassVar[TowerLevelEndNotify.ContinueStateType]
    CONTINUE_STATE_TYPE_CAN_NOT_CONTINUE: TowerLevelEndNotify.ContinueStateType
    CONTINUE_STATE_TYPE_CAN_ENTER_NEXT_LEVEL: TowerLevelEndNotify.ContinueStateType
    CONTINUE_STATE_TYPE_CAN_ENTER_NEXT_FLOOR: TowerLevelEndNotify.ContinueStateType
    REWARD_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_FLOOR_ID_FIELD_NUMBER: _ClassVar[int]
    FINISHED_STAR_COND_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    reward_item_list: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    next_floor_id: int
    finished_star_cond_list: _containers.RepeatedScalarFieldContainer[int]
    continue_state: int
    is_success: bool
    def __init__(self, reward_item_list: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., next_floor_id: _Optional[int] = ..., finished_star_cond_list: _Optional[_Iterable[int]] = ..., continue_state: _Optional[int] = ..., is_success: bool = ...) -> None: ...
