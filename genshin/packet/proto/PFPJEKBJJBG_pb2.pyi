from genshin.packet.proto import OBNKIAPKLNB_pb2 as _OBNKIAPKLNB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PFPJEKBJJBG(_message.Message):
    __slots__ = ("DLCEIFKFFAA", "HHAOEKLDNOL", "ANNCKMOHNLE")
    DLCEIFKFFAA_FIELD_NUMBER: _ClassVar[int]
    HHAOEKLDNOL_FIELD_NUMBER: _ClassVar[int]
    ANNCKMOHNLE_FIELD_NUMBER: _ClassVar[int]
    DLCEIFKFFAA: _containers.RepeatedScalarFieldContainer[int]
    HHAOEKLDNOL: _OBNKIAPKLNB_pb2.OBNKIAPKLNB
    ANNCKMOHNLE: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, DLCEIFKFFAA: _Optional[_Iterable[int]] = ..., HHAOEKLDNOL: _Optional[_Union[_OBNKIAPKLNB_pb2.OBNKIAPKLNB, _Mapping]] = ..., ANNCKMOHNLE: _Optional[_Iterable[int]] = ...) -> None: ...
