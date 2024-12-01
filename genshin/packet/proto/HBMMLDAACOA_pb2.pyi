from genshin.packet.proto import OBNKIAPKLNB_pb2 as _OBNKIAPKLNB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HBMMLDAACOA(_message.Message):
    __slots__ = ("HHAOEKLDNOL", "FBNMBDDBNDH", "DOMBDIMFFII", "MKCGMMGANLK")
    HHAOEKLDNOL_FIELD_NUMBER: _ClassVar[int]
    FBNMBDDBNDH_FIELD_NUMBER: _ClassVar[int]
    DOMBDIMFFII_FIELD_NUMBER: _ClassVar[int]
    MKCGMMGANLK_FIELD_NUMBER: _ClassVar[int]
    HHAOEKLDNOL: _OBNKIAPKLNB_pb2.OBNKIAPKLNB
    FBNMBDDBNDH: _containers.RepeatedScalarFieldContainer[int]
    DOMBDIMFFII: int
    MKCGMMGANLK: int
    def __init__(self, HHAOEKLDNOL: _Optional[_Union[_OBNKIAPKLNB_pb2.OBNKIAPKLNB, _Mapping]] = ..., FBNMBDDBNDH: _Optional[_Iterable[int]] = ..., DOMBDIMFFII: _Optional[int] = ..., MKCGMMGANLK: _Optional[int] = ...) -> None: ...
