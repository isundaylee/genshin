from genshin.packet.proto import PropChangeReason_pb2 as _PropChangeReason_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerPropChangeReasonNotify(_message.Message):
    __slots__ = ("cur_value", "reason", "prop_type", "old_value")
    CUR_VALUE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    cur_value: float
    reason: _PropChangeReason_pb2.PropChangeReason
    prop_type: int
    old_value: float
    def __init__(self, cur_value: _Optional[float] = ..., reason: _Optional[_Union[_PropChangeReason_pb2.PropChangeReason, str]] = ..., prop_type: _Optional[int] = ..., old_value: _Optional[float] = ...) -> None: ...
