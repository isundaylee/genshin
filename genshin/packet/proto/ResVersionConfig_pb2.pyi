from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResVersionConfig(_message.Message):
    __slots__ = ("version", "relogin", "md5", "release_total_size", "version_suffix", "branch", "next_script_version")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RELOGIN_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCRIPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    relogin: bool
    md5: str
    release_total_size: str
    version_suffix: str
    branch: str
    next_script_version: str
    def __init__(self, version: _Optional[int] = ..., relogin: bool = ..., md5: _Optional[str] = ..., release_total_size: _Optional[str] = ..., version_suffix: _Optional[str] = ..., branch: _Optional[str] = ..., next_script_version: _Optional[str] = ...) -> None: ...
