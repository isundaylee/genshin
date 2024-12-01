from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CNHLJKCJAHB(_message.Message):
    __slots__ = ("NBMAECPJEAI", "IANEBDKAMBM", "NCCPPHNNPBF", "DOJLEKIENIL", "GGIGCLLHEFM")
    NBMAECPJEAI_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    DOJLEKIENIL_FIELD_NUMBER: _ClassVar[int]
    GGIGCLLHEFM_FIELD_NUMBER: _ClassVar[int]
    NBMAECPJEAI: str
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    NCCPPHNNPBF: int
    DOJLEKIENIL: int
    GGIGCLLHEFM: int
    def __init__(self, NBMAECPJEAI: _Optional[str] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., NCCPPHNNPBF: _Optional[int] = ..., DOJLEKIENIL: _Optional[int] = ..., GGIGCLLHEFM: _Optional[int] = ...) -> None: ...
