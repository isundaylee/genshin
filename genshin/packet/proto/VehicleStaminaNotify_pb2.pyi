from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleStaminaNotify(_message.Message):
    __slots__ = ("entity_id", "cur_stamina")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_STAMINA_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    cur_stamina: float
    def __init__(self, entity_id: _Optional[int] = ..., cur_stamina: _Optional[float] = ...) -> None: ...
