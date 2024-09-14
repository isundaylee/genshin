from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatInfo(_message.Message):
    __slots__ = ("is_read", "time", "to_uid", "sequence", "uid", "icon", "text", "system_hint")
    class SystemHintType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYSTEM_HINT_TYPE_CHAT_NONE: _ClassVar[ChatInfo.SystemHintType]
        SYSTEM_HINT_TYPE_CHAT_ENTER_WORLD: _ClassVar[ChatInfo.SystemHintType]
        SYSTEM_HINT_TYPE_CHAT_LEAVE_WORLD: _ClassVar[ChatInfo.SystemHintType]
    SYSTEM_HINT_TYPE_CHAT_NONE: ChatInfo.SystemHintType
    SYSTEM_HINT_TYPE_CHAT_ENTER_WORLD: ChatInfo.SystemHintType
    SYSTEM_HINT_TYPE_CHAT_LEAVE_WORLD: ChatInfo.SystemHintType
    class SystemHint(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: int
        def __init__(self, type: _Optional[int] = ...) -> None: ...
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_UID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_HINT_FIELD_NUMBER: _ClassVar[int]
    is_read: bool
    time: int
    to_uid: int
    sequence: int
    uid: int
    icon: int
    text: str
    system_hint: ChatInfo.SystemHint
    def __init__(self, is_read: bool = ..., time: _Optional[int] = ..., to_uid: _Optional[int] = ..., sequence: _Optional[int] = ..., uid: _Optional[int] = ..., icon: _Optional[int] = ..., text: _Optional[str] = ..., system_hint: _Optional[_Union[ChatInfo.SystemHint, _Mapping]] = ...) -> None: ...
