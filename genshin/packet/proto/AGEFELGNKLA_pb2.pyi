from genshin.packet.proto import NKDCCKJAIMD_pb2 as _NKDCCKJAIMD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AGEFELGNKLA(_message.Message):
    __slots__ = ("OMOLHGDOJCH", "ADGGHAHHFDA", "IEJPGHNLIDB", "BDLKBOKNANO", "GLKNGDDNOCN")
    OMOLHGDOJCH_FIELD_NUMBER: _ClassVar[int]
    ADGGHAHHFDA_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    BDLKBOKNANO_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    OMOLHGDOJCH: _containers.RepeatedCompositeFieldContainer[_NKDCCKJAIMD_pb2.NKDCCKJAIMD]
    ADGGHAHHFDA: _containers.RepeatedScalarFieldContainer[int]
    IEJPGHNLIDB: int
    BDLKBOKNANO: int
    GLKNGDDNOCN: bool
    def __init__(self, OMOLHGDOJCH: _Optional[_Iterable[_Union[_NKDCCKJAIMD_pb2.NKDCCKJAIMD, _Mapping]]] = ..., ADGGHAHHFDA: _Optional[_Iterable[int]] = ..., IEJPGHNLIDB: _Optional[int] = ..., BDLKBOKNANO: _Optional[int] = ..., GLKNGDDNOCN: bool = ...) -> None: ...
