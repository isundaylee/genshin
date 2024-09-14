from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerPreEnterMpNotify(_message.Message):
    __slots__ = ("state", "nickname", "uid")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[PlayerPreEnterMpNotify.State]
        START: _ClassVar[PlayerPreEnterMpNotify.State]
        TIMEOUT: _ClassVar[PlayerPreEnterMpNotify.State]
    INVALID: PlayerPreEnterMpNotify.State
    START: PlayerPreEnterMpNotify.State
    TIMEOUT: PlayerPreEnterMpNotify.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    state: PlayerPreEnterMpNotify.State
    nickname: str
    uid: int
    def __init__(self, state: _Optional[_Union[PlayerPreEnterMpNotify.State, str]] = ..., nickname: _Optional[str] = ..., uid: _Optional[int] = ...) -> None: ...
