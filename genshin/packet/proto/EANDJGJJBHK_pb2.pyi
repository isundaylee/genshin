from genshin.packet.proto import LMLBFOELDFF_pb2 as _LMLBFOELDFF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EANDJGJJBHK(_message.Message):
    __slots__ = ("FPKEIGKADAB", "KDMJFHDPPDP", "FINAHGLFHAG", "OIBOOEEAIDH", "CDCHFGFJNOI", "EAIPGEMKNPO")
    FPKEIGKADAB_FIELD_NUMBER: _ClassVar[int]
    KDMJFHDPPDP_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    OIBOOEEAIDH_FIELD_NUMBER: _ClassVar[int]
    CDCHFGFJNOI_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    FPKEIGKADAB: _containers.RepeatedCompositeFieldContainer[_LMLBFOELDFF_pb2.LMLBFOELDFF]
    KDMJFHDPPDP: int
    FINAHGLFHAG: int
    OIBOOEEAIDH: int
    CDCHFGFJNOI: int
    EAIPGEMKNPO: int
    def __init__(self, FPKEIGKADAB: _Optional[_Iterable[_Union[_LMLBFOELDFF_pb2.LMLBFOELDFF, _Mapping]]] = ..., KDMJFHDPPDP: _Optional[int] = ..., FINAHGLFHAG: _Optional[int] = ..., OIBOOEEAIDH: _Optional[int] = ..., CDCHFGFJNOI: _Optional[int] = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...