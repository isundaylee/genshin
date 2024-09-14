from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureBlockInfo(_message.Message):
    __slots__ = ("feature_type", "end_time")
    FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    feature_type: int
    end_time: int
    def __init__(self, feature_type: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
