from genshin.packet.proto import PBEODMMDBGB_pb2 as _PBEODMMDBGB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FIFPJPAGGOD(_message.Message):
    __slots__ = ("PMJGJNILMBP", "EAIPGEMKNPO", "PMJLLLFOPHK", "NMAAPLDBBNI")
    PMJGJNILMBP_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    PMJLLLFOPHK_FIELD_NUMBER: _ClassVar[int]
    NMAAPLDBBNI_FIELD_NUMBER: _ClassVar[int]
    PMJGJNILMBP: _containers.RepeatedCompositeFieldContainer[_PBEODMMDBGB_pb2.PBEODMMDBGB]
    EAIPGEMKNPO: int
    PMJLLLFOPHK: bool
    NMAAPLDBBNI: int
    def __init__(self, PMJGJNILMBP: _Optional[_Iterable[_Union[_PBEODMMDBGB_pb2.PBEODMMDBGB, _Mapping]]] = ..., EAIPGEMKNPO: _Optional[int] = ..., PMJLLLFOPHK: bool = ..., NMAAPLDBBNI: _Optional[int] = ...) -> None: ...
