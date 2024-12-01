from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BOMACPDEPID(_message.Message):
    __slots__ = ("promote_level", "JLGJBALEIOI", "KJFLEHHDMBB", "item_id")
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    JLGJBALEIOI_FIELD_NUMBER: _ClassVar[int]
    KJFLEHHDMBB_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    promote_level: int
    JLGJBALEIOI: int
    KJFLEHHDMBB: int
    item_id: int
    def __init__(self, promote_level: _Optional[int] = ..., JLGJBALEIOI: _Optional[int] = ..., KJFLEHHDMBB: _Optional[int] = ..., item_id: _Optional[int] = ...) -> None: ...
