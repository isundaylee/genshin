from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Achievement(_message.Message):
    __slots__ = ("cur_progress", "total_progress", "finish_timestamp", "status", "id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_INVALID: _ClassVar[Achievement.Status]
        STATUS_UNFINISHED: _ClassVar[Achievement.Status]
        STATUS_FINISHED: _ClassVar[Achievement.Status]
        STATUS_REWARD_TAKEN: _ClassVar[Achievement.Status]
    STATUS_INVALID: Achievement.Status
    STATUS_UNFINISHED: Achievement.Status
    STATUS_FINISHED: Achievement.Status
    STATUS_REWARD_TAKEN: Achievement.Status
    CUR_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    cur_progress: int
    total_progress: int
    finish_timestamp: int
    status: Achievement.Status
    id: int
    def __init__(self, cur_progress: _Optional[int] = ..., total_progress: _Optional[int] = ..., finish_timestamp: _Optional[int] = ..., status: _Optional[_Union[Achievement.Status, str]] = ..., id: _Optional[int] = ...) -> None: ...
