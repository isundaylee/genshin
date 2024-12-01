from genshin.packet.proto import ABCMJCGAJMD_pb2 as _ABCMJCGAJMD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NAKLNGMFLHF(_message.Message):
    __slots__ = ("CCADHOHDBGJ", "DKBOICELOCN", "NCCPPHNNPBF", "JJHDGNFDGDE", "LAHONFCEPNN")
    CCADHOHDBGJ_FIELD_NUMBER: _ClassVar[int]
    DKBOICELOCN_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    JJHDGNFDGDE_FIELD_NUMBER: _ClassVar[int]
    LAHONFCEPNN_FIELD_NUMBER: _ClassVar[int]
    CCADHOHDBGJ: _containers.RepeatedCompositeFieldContainer[_ABCMJCGAJMD_pb2.ABCMJCGAJMD]
    DKBOICELOCN: bool
    NCCPPHNNPBF: int
    JJHDGNFDGDE: int
    LAHONFCEPNN: int
    def __init__(self, CCADHOHDBGJ: _Optional[_Iterable[_Union[_ABCMJCGAJMD_pb2.ABCMJCGAJMD, _Mapping]]] = ..., DKBOICELOCN: bool = ..., NCCPPHNNPBF: _Optional[int] = ..., JJHDGNFDGDE: _Optional[int] = ..., LAHONFCEPNN: _Optional[int] = ...) -> None: ...
