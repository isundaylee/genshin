from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HOBLMOAGLLH(_message.Message):
    __slots__ = ("IANEBDKAMBM", "EFAJIHMNOBK", "OMKNBNMEBIK", "JAHPPELNEDF", "NCCPPHNNPBF", "HOHCJOCIGOK", "ODCPAECONND", "FCPANCMAOIE")
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    HOHCJOCIGOK_FIELD_NUMBER: _ClassVar[int]
    ODCPAECONND_FIELD_NUMBER: _ClassVar[int]
    FCPANCMAOIE_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    EFAJIHMNOBK: str
    OMKNBNMEBIK: str
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    NCCPPHNNPBF: int
    HOHCJOCIGOK: int
    ODCPAECONND: int
    FCPANCMAOIE: int
    def __init__(self, IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., EFAJIHMNOBK: _Optional[str] = ..., OMKNBNMEBIK: _Optional[str] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., NCCPPHNNPBF: _Optional[int] = ..., HOHCJOCIGOK: _Optional[int] = ..., ODCPAECONND: _Optional[int] = ..., FCPANCMAOIE: _Optional[int] = ...) -> None: ...
