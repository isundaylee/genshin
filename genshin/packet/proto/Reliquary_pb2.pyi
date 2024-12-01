from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Reliquary(_message.Message):
    __slots__ = ("append_prop_id_list", "main_prop_id", "level", "promote_level", "exp", "LCEENMIFAPM")
    APPEND_PROP_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    MAIN_PROP_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    LCEENMIFAPM_FIELD_NUMBER: _ClassVar[int]
    append_prop_id_list: _containers.RepeatedScalarFieldContainer[int]
    main_prop_id: int
    level: int
    promote_level: int
    exp: int
    LCEENMIFAPM: bool
    def __init__(self, append_prop_id_list: _Optional[_Iterable[int]] = ..., main_prop_id: _Optional[int] = ..., level: _Optional[int] = ..., promote_level: _Optional[int] = ..., exp: _Optional[int] = ..., LCEENMIFAPM: bool = ...) -> None: ...
