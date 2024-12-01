from genshin.packet.proto import IMGPEMFGOPF_pb2 as _IMGPEMFGOPF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BDGCFPBNAAM(_message.Message):
    __slots__ = ("COKCGKDPPEM", "OAJOOBGHAGM")
    COKCGKDPPEM_FIELD_NUMBER: _ClassVar[int]
    OAJOOBGHAGM_FIELD_NUMBER: _ClassVar[int]
    COKCGKDPPEM: _IMGPEMFGOPF_pb2.IMGPEMFGOPF
    OAJOOBGHAGM: int
    def __init__(self, COKCGKDPPEM: _Optional[_Union[_IMGPEMFGOPF_pb2.IMGPEMFGOPF, str]] = ..., OAJOOBGHAGM: _Optional[int] = ...) -> None: ...
