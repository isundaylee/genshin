from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerQuitFromHomeNotify(_message.Message):
    __slots__ = ("reason",)
    class QuitReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
        KICK_BY_HOST: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
        BACK_TO_MY_WORLD: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
        HOME_BLOCKED: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
        HOME_IN_EDIT_MODE: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
        BY_MUIP: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
        CUR_MODULE_CLOSED: _ClassVar[PlayerQuitFromHomeNotify.QuitReason]
    INVALID: PlayerQuitFromHomeNotify.QuitReason
    KICK_BY_HOST: PlayerQuitFromHomeNotify.QuitReason
    BACK_TO_MY_WORLD: PlayerQuitFromHomeNotify.QuitReason
    HOME_BLOCKED: PlayerQuitFromHomeNotify.QuitReason
    HOME_IN_EDIT_MODE: PlayerQuitFromHomeNotify.QuitReason
    BY_MUIP: PlayerQuitFromHomeNotify.QuitReason
    CUR_MODULE_CLOSED: PlayerQuitFromHomeNotify.QuitReason
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: PlayerQuitFromHomeNotify.QuitReason
    def __init__(self, reason: _Optional[_Union[PlayerQuitFromHomeNotify.QuitReason, str]] = ...) -> None: ...
