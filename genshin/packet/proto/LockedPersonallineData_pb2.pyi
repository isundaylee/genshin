from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LockedPersonallineData(_message.Message):
    __slots__ = ("lock_reason", "personal_line_id", "chapter_id", "level", "quest_param")
    class LockReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LockReason_LEVEL: _ClassVar[LockedPersonallineData.LockReason]
        LockReason_QUEST: _ClassVar[LockedPersonallineData.LockReason]
    LockReason_LEVEL: LockedPersonallineData.LockReason
    LockReason_QUEST: LockedPersonallineData.LockReason
    class QuestParam(_message.Message):
        __slots__ = ("chapter_id", "quest_id")
        CHAPTER_ID_FIELD_NUMBER: _ClassVar[int]
        QUEST_ID_FIELD_NUMBER: _ClassVar[int]
        chapter_id: int
        quest_id: int
        def __init__(self, chapter_id: _Optional[int] = ..., quest_id: _Optional[int] = ...) -> None: ...
    LOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_LINE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAPTER_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    QUEST_PARAM_FIELD_NUMBER: _ClassVar[int]
    lock_reason: LockedPersonallineData.LockReason
    personal_line_id: int
    chapter_id: int
    level: int
    quest_param: LockedPersonallineData.QuestParam
    def __init__(self, lock_reason: _Optional[_Union[LockedPersonallineData.LockReason, str]] = ..., personal_line_id: _Optional[int] = ..., chapter_id: _Optional[int] = ..., level: _Optional[int] = ..., quest_param: _Optional[_Union[LockedPersonallineData.QuestParam, _Mapping]] = ...) -> None: ...
