from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PLIAJBGKCMD(_message.Message):
    __slots__ = ("EFAJIHMNOBK", "OMKNBNMEBIK", "JAHPPELNEDF", "IANEBDKAMBM", "NCCPPHNNPBF")
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK: str
    OMKNBNMEBIK: str
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    NCCPPHNNPBF: int
    def __init__(self, EFAJIHMNOBK: _Optional[str] = ..., OMKNBNMEBIK: _Optional[str] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., NCCPPHNNPBF: _Optional[int] = ...) -> None: ...
