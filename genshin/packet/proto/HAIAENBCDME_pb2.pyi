from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HAIAENBCDME(_message.Message):
    __slots__ = ("OMKNBNMEBIK", "IANEBDKAMBM", "EFAJIHMNOBK", "DOJLEKIENIL", "NCCPPHNNPBF")
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    DOJLEKIENIL_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK: str
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    EFAJIHMNOBK: str
    DOJLEKIENIL: int
    NCCPPHNNPBF: int
    def __init__(self, OMKNBNMEBIK: _Optional[str] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., EFAJIHMNOBK: _Optional[str] = ..., DOJLEKIENIL: _Optional[int] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
