from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientScriptEventNotify(_message.Message):
    __slots__ = ("source_entity_id", "target_entity_id", "event_type", "param_list")
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    source_entity_id: int
    target_entity_id: int
    event_type: int
    param_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, source_entity_id: _Optional[int] = ..., target_entity_id: _Optional[int] = ..., event_type: _Optional[int] = ..., param_list: _Optional[_Iterable[int]] = ...) -> None: ...
