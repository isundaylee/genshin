from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MPOLDIBFEMM(_message.Message):
    __slots__ = ("JNIMCKPLNFH", "avatar_id")
    JNIMCKPLNFH_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    JNIMCKPLNFH: _containers.RepeatedScalarFieldContainer[int]
    avatar_id: int
    def __init__(self, JNIMCKPLNFH: _Optional[_Iterable[int]] = ..., avatar_id: _Optional[int] = ...) -> None: ...
