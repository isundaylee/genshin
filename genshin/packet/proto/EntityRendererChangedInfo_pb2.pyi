from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EntityRendererChangedInfo(_message.Message):
    __slots__ = ("changed_renderers", "visibility_count", "is_cached")
    class ChangedRenderersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CHANGED_RENDERERS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_CACHED_FIELD_NUMBER: _ClassVar[int]
    changed_renderers: _containers.ScalarMap[str, int]
    visibility_count: int
    is_cached: bool
    def __init__(self, changed_renderers: _Optional[_Mapping[str, int]] = ..., visibility_count: _Optional[int] = ..., is_cached: bool = ...) -> None: ...
