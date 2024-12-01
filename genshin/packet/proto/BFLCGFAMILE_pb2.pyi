from genshin.packet.proto import KNMPNCPBMMP_pb2 as _KNMPNCPBMMP_pb2
from genshin.packet.proto import FJCOKOHBJIN_pb2 as _FJCOKOHBJIN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BFLCGFAMILE(_message.Message):
    __slots__ = ("MJAONINHIIB", "MEOGIFMOGGM", "FJOAEEMIBAE", "BCKBKIDDFCD", "MEJLFKPFPGK", "DBHIFKIIEOI", "EMKABKLDMAN", "FLIOFBBOPPB")
    MJAONINHIIB_FIELD_NUMBER: _ClassVar[int]
    MEOGIFMOGGM_FIELD_NUMBER: _ClassVar[int]
    FJOAEEMIBAE_FIELD_NUMBER: _ClassVar[int]
    BCKBKIDDFCD_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    DBHIFKIIEOI_FIELD_NUMBER: _ClassVar[int]
    EMKABKLDMAN_FIELD_NUMBER: _ClassVar[int]
    FLIOFBBOPPB_FIELD_NUMBER: _ClassVar[int]
    MJAONINHIIB: _containers.RepeatedScalarFieldContainer[int]
    MEOGIFMOGGM: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    FJOAEEMIBAE: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    BCKBKIDDFCD: _containers.RepeatedCompositeFieldContainer[_FJCOKOHBJIN_pb2.FJCOKOHBJIN]
    MEJLFKPFPGK: int
    DBHIFKIIEOI: int
    EMKABKLDMAN: int
    FLIOFBBOPPB: int
    def __init__(self, MJAONINHIIB: _Optional[_Iterable[int]] = ..., MEOGIFMOGGM: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., FJOAEEMIBAE: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., BCKBKIDDFCD: _Optional[_Iterable[_Union[_FJCOKOHBJIN_pb2.FJCOKOHBJIN, _Mapping]]] = ..., MEJLFKPFPGK: _Optional[int] = ..., DBHIFKIIEOI: _Optional[int] = ..., EMKABKLDMAN: _Optional[int] = ..., FLIOFBBOPPB: _Optional[int] = ...) -> None: ...
