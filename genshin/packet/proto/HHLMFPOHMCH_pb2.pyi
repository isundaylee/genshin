from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HHLMFPOHMCH(_message.Message):
    __slots__ = ("MHGCJHMBJDJ", "CBFLKNIMPPM", "HLKDDNGCKJN", "PMJLLLFOPHK", "CPOHJLECLOK", "EHAEACFBOOL", "ADJNOLPLKOA")
    class MHGCJHMBJDJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MHGCJHMBJDJ_FIELD_NUMBER: _ClassVar[int]
    CBFLKNIMPPM_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    PMJLLLFOPHK_FIELD_NUMBER: _ClassVar[int]
    CPOHJLECLOK_FIELD_NUMBER: _ClassVar[int]
    EHAEACFBOOL_FIELD_NUMBER: _ClassVar[int]
    ADJNOLPLKOA_FIELD_NUMBER: _ClassVar[int]
    MHGCJHMBJDJ: _containers.ScalarMap[int, int]
    CBFLKNIMPPM: int
    HLKDDNGCKJN: int
    PMJLLLFOPHK: bool
    CPOHJLECLOK: bool
    EHAEACFBOOL: int
    ADJNOLPLKOA: int
    def __init__(self, MHGCJHMBJDJ: _Optional[_Mapping[int, int]] = ..., CBFLKNIMPPM: _Optional[int] = ..., HLKDDNGCKJN: _Optional[int] = ..., PMJLLLFOPHK: bool = ..., CPOHJLECLOK: bool = ..., EHAEACFBOOL: _Optional[int] = ..., ADJNOLPLKOA: _Optional[int] = ...) -> None: ...
