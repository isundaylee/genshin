from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteGadgetLuaReq(_message.Message):
    __slots__ = ("param1", "param3", "source_entity_id", "param2", "BMDLHCMBPOA")
    PARAM1_FIELD_NUMBER: _ClassVar[int]
    PARAM3_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARAM2_FIELD_NUMBER: _ClassVar[int]
    BMDLHCMBPOA_FIELD_NUMBER: _ClassVar[int]
    param1: int
    param3: int
    source_entity_id: int
    param2: int
    BMDLHCMBPOA: str
    def __init__(self, param1: _Optional[int] = ..., param3: _Optional[int] = ..., source_entity_id: _Optional[int] = ..., param2: _Optional[int] = ..., BMDLHCMBPOA: _Optional[str] = ...) -> None: ...
