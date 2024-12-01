from genshin.packet.proto import CGAALGDLEHL_pb2 as _CGAALGDLEHL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FKDDDHIEGMF(_message.Message):
    __slots__ = ("CGIELIFMPLC", "ADGGHAHHFDA", "PIEAPGEPMLF", "BDLKBOKNANO")
    CGIELIFMPLC_FIELD_NUMBER: _ClassVar[int]
    ADGGHAHHFDA_FIELD_NUMBER: _ClassVar[int]
    PIEAPGEPMLF_FIELD_NUMBER: _ClassVar[int]
    BDLKBOKNANO_FIELD_NUMBER: _ClassVar[int]
    CGIELIFMPLC: _containers.RepeatedCompositeFieldContainer[_CGAALGDLEHL_pb2.CGAALGDLEHL]
    ADGGHAHHFDA: _containers.RepeatedScalarFieldContainer[int]
    PIEAPGEPMLF: int
    BDLKBOKNANO: int
    def __init__(self, CGIELIFMPLC: _Optional[_Iterable[_Union[_CGAALGDLEHL_pb2.CGAALGDLEHL, _Mapping]]] = ..., ADGGHAHHFDA: _Optional[_Iterable[int]] = ..., PIEAPGEPMLF: _Optional[int] = ..., BDLKBOKNANO: _Optional[int] = ...) -> None: ...
