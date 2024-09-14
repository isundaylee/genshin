from genshin.packet.proto import BreakoutVector2_pb2 as _BreakoutVector2_pb2
from genshin.packet.proto import BreakoutPhysicalObjectModifier_pb2 as _BreakoutPhysicalObjectModifier_pb2
from genshin.packet.proto import BreakoutBrickInfo_pb2 as _BreakoutBrickInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutPhysicalObject(_message.Message):
    __slots__ = ("id", "index", "is_active", "pos", "move_dir", "speed", "init_peer_id", "state", "element_type", "element_reaction_buff", "modifier_list", "total_rotation", "info_list", "last_hit_peer_id", "speed_increase_count", "offset")
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MOVE_DIR_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    INIT_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_REACTION_BUFF_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROTATION_FIELD_NUMBER: _ClassVar[int]
    INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    LAST_HIT_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    SPEED_INCREASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    id: int
    index: int
    is_active: bool
    pos: _BreakoutVector2_pb2.BreakoutVector2
    move_dir: _BreakoutVector2_pb2.BreakoutVector2
    speed: int
    init_peer_id: int
    state: int
    element_type: int
    element_reaction_buff: int
    modifier_list: _containers.RepeatedCompositeFieldContainer[_BreakoutPhysicalObjectModifier_pb2.BreakoutPhysicalObjectModifier]
    total_rotation: int
    info_list: _containers.RepeatedCompositeFieldContainer[_BreakoutBrickInfo_pb2.BreakoutBrickInfo]
    last_hit_peer_id: int
    speed_increase_count: int
    offset: int
    def __init__(self, id: _Optional[int] = ..., index: _Optional[int] = ..., is_active: bool = ..., pos: _Optional[_Union[_BreakoutVector2_pb2.BreakoutVector2, _Mapping]] = ..., move_dir: _Optional[_Union[_BreakoutVector2_pb2.BreakoutVector2, _Mapping]] = ..., speed: _Optional[int] = ..., init_peer_id: _Optional[int] = ..., state: _Optional[int] = ..., element_type: _Optional[int] = ..., element_reaction_buff: _Optional[int] = ..., modifier_list: _Optional[_Iterable[_Union[_BreakoutPhysicalObjectModifier_pb2.BreakoutPhysicalObjectModifier, _Mapping]]] = ..., total_rotation: _Optional[int] = ..., info_list: _Optional[_Iterable[_Union[_BreakoutBrickInfo_pb2.BreakoutBrickInfo, _Mapping]]] = ..., last_hit_peer_id: _Optional[int] = ..., speed_increase_count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...
