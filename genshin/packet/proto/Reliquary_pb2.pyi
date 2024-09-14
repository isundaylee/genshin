from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Reliquary(_message.Message):
    __slots__ = ("level", "exp", "promote_level", "main_prop_id", "append_prop_id_list")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAIN_PROP_ID_FIELD_NUMBER: _ClassVar[int]
    APPEND_PROP_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    level: int
    exp: int
    promote_level: int
    main_prop_id: int
    append_prop_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, level: _Optional[int] = ..., exp: _Optional[int] = ..., promote_level: _Optional[int] = ..., main_prop_id: _Optional[int] = ..., append_prop_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
