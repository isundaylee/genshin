from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetScenePointRsp(_message.Message):
    __slots__ = ("unlocked_point_list", "FELMBEACBLB", "locked_point_list", "point_list", "belong_uid", "retcode", "scene_id", "unhide_point_list", "BEOCPMCPHJH", "DOGJLOBEEPC", "unlock_area_list", "OGLOLEOEAGD", "is_new_player")
    UNLOCKED_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    FELMBEACBLB_FIELD_NUMBER: _ClassVar[int]
    LOCKED_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    BELONG_UID_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    UNHIDE_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    BEOCPMCPHJH_FIELD_NUMBER: _ClassVar[int]
    DOGJLOBEEPC_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_AREA_LIST_FIELD_NUMBER: _ClassVar[int]
    OGLOLEOEAGD_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_PLAYER_FIELD_NUMBER: _ClassVar[int]
    unlocked_point_list: _containers.RepeatedScalarFieldContainer[int]
    FELMBEACBLB: _containers.RepeatedScalarFieldContainer[int]
    locked_point_list: _containers.RepeatedScalarFieldContainer[int]
    point_list: _containers.RepeatedScalarFieldContainer[int]
    belong_uid: int
    retcode: int
    scene_id: int
    unhide_point_list: _containers.RepeatedScalarFieldContainer[int]
    BEOCPMCPHJH: _containers.RepeatedScalarFieldContainer[int]
    DOGJLOBEEPC: _containers.RepeatedScalarFieldContainer[int]
    unlock_area_list: _containers.RepeatedScalarFieldContainer[int]
    OGLOLEOEAGD: _containers.RepeatedScalarFieldContainer[int]
    is_new_player: bool
    def __init__(self, unlocked_point_list: _Optional[_Iterable[int]] = ..., FELMBEACBLB: _Optional[_Iterable[int]] = ..., locked_point_list: _Optional[_Iterable[int]] = ..., point_list: _Optional[_Iterable[int]] = ..., belong_uid: _Optional[int] = ..., retcode: _Optional[int] = ..., scene_id: _Optional[int] = ..., unhide_point_list: _Optional[_Iterable[int]] = ..., BEOCPMCPHJH: _Optional[_Iterable[int]] = ..., DOGJLOBEEPC: _Optional[_Iterable[int]] = ..., unlock_area_list: _Optional[_Iterable[int]] = ..., OGLOLEOEAGD: _Optional[_Iterable[int]] = ..., is_new_player: bool = ...) -> None: ...
