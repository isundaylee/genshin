from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllUnlockNameCardRsp(_message.Message):
    __slots__ = ("retcode", "name_card_list")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    NAME_CARD_LIST_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    name_card_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, retcode: _Optional[int] = ..., name_card_list: _Optional[_Iterable[int]] = ...) -> None: ...
