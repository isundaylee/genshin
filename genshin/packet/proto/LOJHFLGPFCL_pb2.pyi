from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LOJHFLGPFCL(_message.Message):
    __slots__ = ("IJLFKCCOONM", "BMFKOONMMEE", "OMKNBNMEBIK", "IANEBDKAMBM", "MLGFPGIDGNO", "PFBJFCMONKP", "NCCPPHNNPBF", "HECDFNOFPPD")
    class IJLFKCCOONMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IJLFKCCOONM_FIELD_NUMBER: _ClassVar[int]
    BMFKOONMMEE_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    MLGFPGIDGNO_FIELD_NUMBER: _ClassVar[int]
    PFBJFCMONKP_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    HECDFNOFPPD_FIELD_NUMBER: _ClassVar[int]
    IJLFKCCOONM: _containers.ScalarMap[int, int]
    BMFKOONMMEE: str
    OMKNBNMEBIK: str
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    MLGFPGIDGNO: int
    PFBJFCMONKP: bool
    NCCPPHNNPBF: int
    HECDFNOFPPD: int
    def __init__(self, IJLFKCCOONM: _Optional[_Mapping[int, int]] = ..., BMFKOONMMEE: _Optional[str] = ..., OMKNBNMEBIK: _Optional[str] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., MLGFPGIDGNO: _Optional[int] = ..., PFBJFCMONKP: bool = ..., NCCPPHNNPBF: _Optional[int] = ..., HECDFNOFPPD: _Optional[int] = ...) -> None: ...
