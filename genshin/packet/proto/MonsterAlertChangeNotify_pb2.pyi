from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterAlertChangeNotify(_message.Message):
    __slots__ = ("avatar_entity_id", "is_alert", "monster_entity_list")
    AVATAR_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ALERT_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ENTITY_LIST_FIELD_NUMBER: _ClassVar[int]
    avatar_entity_id: int
    is_alert: int
    monster_entity_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, avatar_entity_id: _Optional[int] = ..., is_alert: _Optional[int] = ..., monster_entity_list: _Optional[_Iterable[int]] = ...) -> None: ...
