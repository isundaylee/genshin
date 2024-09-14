from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterMpResultNotify(_message.Message):
    __slots__ = ("reason", "target_nickname", "target_uid", "is_agreed")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_PLAYER_JUDGE: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_SCENE_CANNOT_ENTER: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_PLAYER_CANNOT_ENTER_MP: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_SYSTEM_JUDGE: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_ALLOW_ENTER_PLAYER_FULL: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_WORLD_LEVEL_LOWER_THAN_HOST: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_HOST_IN_MATCH: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_PLAYER_IN_BLACKLIST: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_PS_PLAYER_NOT_ACCEPT_OTHERS: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_HOST_IS_BLOCKED: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_OTHER_DATA_VERSION_NOT_LATEST: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_DATA_VERSION_NOT_LATEST: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_PLAYER_NOT_IN_PLAYER_WORLD: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
        REASON_MAX_PLAYER: _ClassVar[PlayerApplyEnterMpResultNotify.Reason]
    REASON_PLAYER_JUDGE: PlayerApplyEnterMpResultNotify.Reason
    REASON_SCENE_CANNOT_ENTER: PlayerApplyEnterMpResultNotify.Reason
    REASON_PLAYER_CANNOT_ENTER_MP: PlayerApplyEnterMpResultNotify.Reason
    REASON_SYSTEM_JUDGE: PlayerApplyEnterMpResultNotify.Reason
    REASON_ALLOW_ENTER_PLAYER_FULL: PlayerApplyEnterMpResultNotify.Reason
    REASON_WORLD_LEVEL_LOWER_THAN_HOST: PlayerApplyEnterMpResultNotify.Reason
    REASON_HOST_IN_MATCH: PlayerApplyEnterMpResultNotify.Reason
    REASON_PLAYER_IN_BLACKLIST: PlayerApplyEnterMpResultNotify.Reason
    REASON_PS_PLAYER_NOT_ACCEPT_OTHERS: PlayerApplyEnterMpResultNotify.Reason
    REASON_HOST_IS_BLOCKED: PlayerApplyEnterMpResultNotify.Reason
    REASON_OTHER_DATA_VERSION_NOT_LATEST: PlayerApplyEnterMpResultNotify.Reason
    REASON_DATA_VERSION_NOT_LATEST: PlayerApplyEnterMpResultNotify.Reason
    REASON_PLAYER_NOT_IN_PLAYER_WORLD: PlayerApplyEnterMpResultNotify.Reason
    REASON_MAX_PLAYER: PlayerApplyEnterMpResultNotify.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    TARGET_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    IS_AGREED_FIELD_NUMBER: _ClassVar[int]
    reason: PlayerApplyEnterMpResultNotify.Reason
    target_nickname: str
    target_uid: int
    is_agreed: bool
    def __init__(self, reason: _Optional[_Union[PlayerApplyEnterMpResultNotify.Reason, str]] = ..., target_nickname: _Optional[str] = ..., target_uid: _Optional[int] = ..., is_agreed: bool = ...) -> None: ...
