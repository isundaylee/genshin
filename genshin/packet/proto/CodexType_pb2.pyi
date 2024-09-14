from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CodexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CODEX_NONE: _ClassVar[CodexType]
    CODEX_QUEST: _ClassVar[CodexType]
    CODEX_WEAPON: _ClassVar[CodexType]
    CODEX_ANIMAL: _ClassVar[CodexType]
    CODEX_MATERIAL: _ClassVar[CodexType]
    CODEX_BOOKS: _ClassVar[CodexType]
    CODEX_PUSHTIPS: _ClassVar[CodexType]
    CODEX_VIEW: _ClassVar[CodexType]
    CODEX_RELIQUARY: _ClassVar[CodexType]
CODEX_NONE: CodexType
CODEX_QUEST: CodexType
CODEX_WEAPON: CodexType
CODEX_ANIMAL: CodexType
CODEX_MATERIAL: CodexType
CODEX_BOOKS: CodexType
CODEX_PUSHTIPS: CodexType
CODEX_VIEW: CodexType
CODEX_RELIQUARY: CodexType
