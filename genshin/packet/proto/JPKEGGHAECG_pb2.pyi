from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JPKEGGHAECG(_message.Message):
    __slots__ = ("GBHBBLGHDLJ", "DKHHPAJBJIF", "BMFKOONMMEE", "OMKNBNMEBIK", "IANEBDKAMBM", "avatar_id", "NCCPPHNNPBF")
    class GBHBBLGHDLJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GBHBBLGHDLJ_FIELD_NUMBER: _ClassVar[int]
    DKHHPAJBJIF_FIELD_NUMBER: _ClassVar[int]
    BMFKOONMMEE_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    GBHBBLGHDLJ: _containers.ScalarMap[int, int]
    DKHHPAJBJIF: str
    BMFKOONMMEE: str
    OMKNBNMEBIK: str
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    avatar_id: int
    NCCPPHNNPBF: int
    def __init__(self, GBHBBLGHDLJ: _Optional[_Mapping[int, int]] = ..., DKHHPAJBJIF: _Optional[str] = ..., BMFKOONMMEE: _Optional[str] = ..., OMKNBNMEBIK: _Optional[str] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., avatar_id: _Optional[int] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
