from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetNameCardRsp(_message.Message):
    __slots__ = ("retcode", "name_card_id")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    NAME_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    name_card_id: int
    def __init__(self, retcode: _Optional[int] = ..., name_card_id: _Optional[int] = ...) -> None: ...
