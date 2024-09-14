from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetInvestigationMonsterReq(_message.Message):
    __slots__ = ("is_for_mark", "city_id_list")
    IS_FOR_MARK_FIELD_NUMBER: _ClassVar[int]
    CITY_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    is_for_mark: bool
    city_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, is_for_mark: bool = ..., city_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
