from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HJKEEJMIMJM(_message.Message):
    __slots__ = ("FBHBHEAOMMC", "IANEBDKAMBM", "OMKNBNMEBIK", "NCCPPHNNPBF")
    FBHBHEAOMMC_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    FBHBHEAOMMC: _containers.RepeatedScalarFieldContainer[int]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    OMKNBNMEBIK: str
    NCCPPHNNPBF: int
    def __init__(self, FBHBHEAOMMC: _Optional[_Iterable[int]] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., OMKNBNMEBIK: _Optional[str] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
