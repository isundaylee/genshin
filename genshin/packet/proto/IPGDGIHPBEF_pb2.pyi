from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPGDGIHPBEF(_message.Message):
    __slots__ = ("IANEBDKAMBM", "OMKNBNMEBIK", "HBKGBNKKCBG", "NCCPPHNNPBF")
    class HBKGBNKKCBGEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    HBKGBNKKCBG_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    OMKNBNMEBIK: str
    HBKGBNKKCBG: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    def __init__(self, IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., OMKNBNMEBIK: _Optional[str] = ..., HBKGBNKKCBG: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
