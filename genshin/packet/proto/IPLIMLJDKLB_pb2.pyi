from genshin.packet.proto import CGAIDECBEHG_pb2 as _CGAIDECBEHG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPLIMLJDKLB(_message.Message):
    __slots__ = ("DJHMNIDJLCP", "GLKNGDDNOCN", "PMJLLLFOPHK", "EAIPGEMKNPO")
    DJHMNIDJLCP_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    PMJLLLFOPHK_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    DJHMNIDJLCP: _containers.RepeatedCompositeFieldContainer[_CGAIDECBEHG_pb2.CGAIDECBEHG]
    GLKNGDDNOCN: bool
    PMJLLLFOPHK: bool
    EAIPGEMKNPO: int
    def __init__(self, DJHMNIDJLCP: _Optional[_Iterable[_Union[_CGAIDECBEHG_pb2.CGAIDECBEHG, _Mapping]]] = ..., GLKNGDDNOCN: bool = ..., PMJLLLFOPHK: bool = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
