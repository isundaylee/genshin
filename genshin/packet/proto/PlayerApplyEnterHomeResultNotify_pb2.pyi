from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerApplyEnterHomeResultNotify(_message.Message):
    __slots__ = ("is_agreed", "target_nickname", "target_uid", "reason")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAYER_JUDGE: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        PLAYER_ENTER_OPTION_REFUSE: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        PLAYER_ENTER_OPTION_DIRECT: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        SYSTEM_JUDGE: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        HOST_IN_MATCH: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        PS_PLAYER_NOT_ACCEPT_OTHERS: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        OPEN_STATE_NOT_OPEN: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        HOST_IN_EDIT_MODE: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
        PRIOR_CHECK: _ClassVar[PlayerApplyEnterHomeResultNotify.Reason]
    PLAYER_JUDGE: PlayerApplyEnterHomeResultNotify.Reason
    PLAYER_ENTER_OPTION_REFUSE: PlayerApplyEnterHomeResultNotify.Reason
    PLAYER_ENTER_OPTION_DIRECT: PlayerApplyEnterHomeResultNotify.Reason
    SYSTEM_JUDGE: PlayerApplyEnterHomeResultNotify.Reason
    HOST_IN_MATCH: PlayerApplyEnterHomeResultNotify.Reason
    PS_PLAYER_NOT_ACCEPT_OTHERS: PlayerApplyEnterHomeResultNotify.Reason
    OPEN_STATE_NOT_OPEN: PlayerApplyEnterHomeResultNotify.Reason
    HOST_IN_EDIT_MODE: PlayerApplyEnterHomeResultNotify.Reason
    PRIOR_CHECK: PlayerApplyEnterHomeResultNotify.Reason
    IS_AGREED_FIELD_NUMBER: _ClassVar[int]
    TARGET_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_UID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    is_agreed: bool
    target_nickname: str
    target_uid: int
    reason: PlayerApplyEnterHomeResultNotify.Reason
    def __init__(self, is_agreed: bool = ..., target_nickname: _Optional[str] = ..., target_uid: _Optional[int] = ..., reason: _Optional[_Union[PlayerApplyEnterHomeResultNotify.Reason, str]] = ...) -> None: ...
