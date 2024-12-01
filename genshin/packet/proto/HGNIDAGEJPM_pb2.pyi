from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HGNIDAGEJPM(_message.Message):
    __slots__ = ("IANEBDKAMBM", "HBNDFNAKNGK", "NBAMEBAMMNF", "NCCPPHNNPBF", "LJKPFEOOHDI")
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    HBNDFNAKNGK_FIELD_NUMBER: _ClassVar[int]
    NBAMEBAMMNF_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    LJKPFEOOHDI_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    HBNDFNAKNGK: int
    NBAMEBAMMNF: int
    NCCPPHNNPBF: int
    LJKPFEOOHDI: int
    def __init__(self, IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., HBNDFNAKNGK: _Optional[int] = ..., NBAMEBAMMNF: _Optional[int] = ..., NCCPPHNNPBF: _Optional[int] = ..., LJKPFEOOHDI: _Optional[int] = ...) -> None: ...
