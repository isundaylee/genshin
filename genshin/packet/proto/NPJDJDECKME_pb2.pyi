from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NPJDJDECKME(_message.Message):
    __slots__ = ("item_id", "JLGJBALEIOI")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    JLGJBALEIOI_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    JLGJBALEIOI: int
    def __init__(self, item_id: _Optional[int] = ..., JLGJBALEIOI: _Optional[int] = ...) -> None: ...
