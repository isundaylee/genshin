from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ELHHGIEOICP(_message.Message):
    __slots__ = ("OMKNBNMEBIK", "JAHPPELNEDF", "EFAJIHMNOBK", "IANEBDKAMBM", "NCCPPHNNPBF", "ODCPAECONND")
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    ODCPAECONND_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK: str
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    EFAJIHMNOBK: str
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    NCCPPHNNPBF: int
    ODCPAECONND: int
    def __init__(self, OMKNBNMEBIK: _Optional[str] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., EFAJIHMNOBK: _Optional[str] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., NCCPPHNNPBF: _Optional[int] = ..., ODCPAECONND: _Optional[int] = ...) -> None: ...
