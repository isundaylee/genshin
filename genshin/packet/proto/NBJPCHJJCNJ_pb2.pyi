from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NBJPCHJJCNJ(_message.Message):
    __slots__ = ("costume_id", "avatar_id", "OMKNBNMEBIK", "FIEKPELIKLE", "NCCPPHNNPBF", "HDNILDCEFMG", "GGOECIGKPAA")
    COSTUME_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    FIEKPELIKLE_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    HDNILDCEFMG_FIELD_NUMBER: _ClassVar[int]
    GGOECIGKPAA_FIELD_NUMBER: _ClassVar[int]
    costume_id: _containers.RepeatedScalarFieldContainer[int]
    avatar_id: _containers.RepeatedScalarFieldContainer[int]
    OMKNBNMEBIK: str
    FIEKPELIKLE: _containers.RepeatedScalarFieldContainer[int]
    NCCPPHNNPBF: int
    HDNILDCEFMG: bool
    GGOECIGKPAA: bool
    def __init__(self, costume_id: _Optional[_Iterable[int]] = ..., avatar_id: _Optional[_Iterable[int]] = ..., OMKNBNMEBIK: _Optional[str] = ..., FIEKPELIKLE: _Optional[_Iterable[int]] = ..., NCCPPHNNPBF: _Optional[int] = ..., HDNILDCEFMG: bool = ..., GGOECIGKPAA: bool = ...) -> None: ...
