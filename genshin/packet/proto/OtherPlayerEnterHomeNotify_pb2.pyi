from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OtherPlayerEnterHomeNotify(_message.Message):
    __slots__ = ("nickname", "reason")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[OtherPlayerEnterHomeNotify.Reason]
        ENTER: _ClassVar[OtherPlayerEnterHomeNotify.Reason]
        LEAVE: _ClassVar[OtherPlayerEnterHomeNotify.Reason]
    INVALID: OtherPlayerEnterHomeNotify.Reason
    ENTER: OtherPlayerEnterHomeNotify.Reason
    LEAVE: OtherPlayerEnterHomeNotify.Reason
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    reason: OtherPlayerEnterHomeNotify.Reason
    def __init__(self, nickname: _Optional[str] = ..., reason: _Optional[_Union[OtherPlayerEnterHomeNotify.Reason, str]] = ...) -> None: ...
