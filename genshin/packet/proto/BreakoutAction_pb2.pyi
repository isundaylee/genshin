from genshin.packet.proto import BreakoutActionType_pb2 as _BreakoutActionType_pb2
from genshin.packet.proto import BreakoutVector2_pb2 as _BreakoutVector2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutAction(_message.Message):
    __slots__ = ("action_type", "client_game_time", "server_game_time", "is_failed", "pre_index", "new_index", "pos", "move_dir", "speed", "peer_id", "element_type", "element_reaction_buff", "speed_increase_count", "has_extra_ball", "extra_ball_dir", "extra_ball_index", "offset", "CLKEPICNJJD")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_FAILED_FIELD_NUMBER: _ClassVar[int]
    PRE_INDEX_FIELD_NUMBER: _ClassVar[int]
    NEW_INDEX_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MOVE_DIR_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_REACTION_BUFF_FIELD_NUMBER: _ClassVar[int]
    SPEED_INCREASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_EXTRA_BALL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_BALL_DIR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_BALL_INDEX_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CLKEPICNJJD_FIELD_NUMBER: _ClassVar[int]
    action_type: _BreakoutActionType_pb2.BreakoutActionType
    client_game_time: int
    server_game_time: int
    is_failed: bool
    pre_index: int
    new_index: int
    pos: _BreakoutVector2_pb2.BreakoutVector2
    move_dir: _BreakoutVector2_pb2.BreakoutVector2
    speed: int
    peer_id: int
    element_type: int
    element_reaction_buff: int
    speed_increase_count: int
    has_extra_ball: bool
    extra_ball_dir: _BreakoutVector2_pb2.BreakoutVector2
    extra_ball_index: int
    offset: int
    CLKEPICNJJD: int
    def __init__(self, action_type: _Optional[_Union[_BreakoutActionType_pb2.BreakoutActionType, str]] = ..., client_game_time: _Optional[int] = ..., server_game_time: _Optional[int] = ..., is_failed: bool = ..., pre_index: _Optional[int] = ..., new_index: _Optional[int] = ..., pos: _Optional[_Union[_BreakoutVector2_pb2.BreakoutVector2, _Mapping]] = ..., move_dir: _Optional[_Union[_BreakoutVector2_pb2.BreakoutVector2, _Mapping]] = ..., speed: _Optional[int] = ..., peer_id: _Optional[int] = ..., element_type: _Optional[int] = ..., element_reaction_buff: _Optional[int] = ..., speed_increase_count: _Optional[int] = ..., has_extra_ball: bool = ..., extra_ball_dir: _Optional[_Union[_BreakoutVector2_pb2.BreakoutVector2, _Mapping]] = ..., extra_ball_index: _Optional[int] = ..., offset: _Optional[int] = ..., CLKEPICNJJD: _Optional[int] = ...) -> None: ...
