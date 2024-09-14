from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RoguelikeGadgetInfo(_message.Message):
    __slots__ = ("cell_config_id", "cell_type", "cell_state", "cell_id")
    CELL_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CELL_STATE_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    cell_config_id: int
    cell_type: int
    cell_state: int
    cell_id: int
    def __init__(self, cell_config_id: _Optional[int] = ..., cell_type: _Optional[int] = ..., cell_state: _Optional[int] = ..., cell_id: _Optional[int] = ...) -> None: ...
