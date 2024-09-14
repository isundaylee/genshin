from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueryCodexMonsterBeKilledNumRsp(_message.Message):
    __slots__ = ("be_killed_num_list", "be_captured_num_list", "retcode", "codex_id_list")
    BE_KILLED_NUM_LIST_FIELD_NUMBER: _ClassVar[int]
    BE_CAPTURED_NUM_LIST_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    CODEX_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    be_killed_num_list: _containers.RepeatedScalarFieldContainer[int]
    be_captured_num_list: _containers.RepeatedScalarFieldContainer[int]
    retcode: int
    codex_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, be_killed_num_list: _Optional[_Iterable[int]] = ..., be_captured_num_list: _Optional[_Iterable[int]] = ..., retcode: _Optional[int] = ..., codex_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
