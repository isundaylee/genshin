from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetNameCardReq(_message.Message):
    __slots__ = ("name_card_id",)
    NAME_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    name_card_id: int
    def __init__(self, name_card_id: _Optional[int] = ...) -> None: ...
