from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChapterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAPTER_STATE_INVALID: _ClassVar[ChapterState]
    CHAPTER_STATE_UNABLE_TO_BEGIN: _ClassVar[ChapterState]
    CHAPTER_STATE_BEGIN: _ClassVar[ChapterState]
    CHAPTER_STATE_END: _ClassVar[ChapterState]
CHAPTER_STATE_INVALID: ChapterState
CHAPTER_STATE_UNABLE_TO_BEGIN: ChapterState
CHAPTER_STATE_BEGIN: ChapterState
CHAPTER_STATE_END: ChapterState
