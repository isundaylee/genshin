from genshin.packet.proto import OAODPGJOMPF_pb2 as _OAODPGJOMPF_pb2
from genshin.packet.proto import KPFOBLALBLC_pb2 as _KPFOBLALBLC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CFIGFKCGJHA(_message.Message):
    __slots__ = ("CIDMBDPHCHJ", "EJNINFFFKJP", "DAAKPCOABEP")
    CIDMBDPHCHJ_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DAAKPCOABEP_FIELD_NUMBER: _ClassVar[int]
    CIDMBDPHCHJ: _containers.RepeatedCompositeFieldContainer[_OAODPGJOMPF_pb2.OAODPGJOMPF]
    EJNINFFFKJP: int
    DAAKPCOABEP: _KPFOBLALBLC_pb2.KPFOBLALBLC
    def __init__(self, CIDMBDPHCHJ: _Optional[_Iterable[_Union[_OAODPGJOMPF_pb2.OAODPGJOMPF, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., DAAKPCOABEP: _Optional[_Union[_KPFOBLALBLC_pb2.KPFOBLALBLC, str]] = ...) -> None: ...
