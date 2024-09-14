from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BreakoutPhysicalObjectModifier(_message.Message):
    __slots__ = ("type", "id", "param1", "param2", "param3", "param4", "param5", "param6", "bool1", "duration", "end_time", "combo", "peer_id", "skill_type", "level", "choose_player_count")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARAM1_FIELD_NUMBER: _ClassVar[int]
    PARAM2_FIELD_NUMBER: _ClassVar[int]
    PARAM3_FIELD_NUMBER: _ClassVar[int]
    PARAM4_FIELD_NUMBER: _ClassVar[int]
    PARAM5_FIELD_NUMBER: _ClassVar[int]
    PARAM6_FIELD_NUMBER: _ClassVar[int]
    BOOL1_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    COMBO_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_PLAYER_COUNT_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    param1: int
    param2: int
    param3: int
    param4: int
    param5: int
    param6: int
    bool1: bool
    duration: int
    end_time: int
    combo: int
    peer_id: int
    skill_type: int
    level: int
    choose_player_count: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., param1: _Optional[int] = ..., param2: _Optional[int] = ..., param3: _Optional[int] = ..., param4: _Optional[int] = ..., param5: _Optional[int] = ..., param6: _Optional[int] = ..., bool1: bool = ..., duration: _Optional[int] = ..., end_time: _Optional[int] = ..., combo: _Optional[int] = ..., peer_id: _Optional[int] = ..., skill_type: _Optional[int] = ..., level: _Optional[int] = ..., choose_player_count: _Optional[int] = ...) -> None: ...
