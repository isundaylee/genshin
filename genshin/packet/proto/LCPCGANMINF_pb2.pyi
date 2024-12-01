from genshin.packet.proto import PHDAEEHJBBA_pb2 as _PHDAEEHJBBA_pb2
from genshin.packet.proto import GFINLGDCIIN_pb2 as _GFINLGDCIIN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LCPCGANMINF(_message.Message):
    __slots__ = ("BJDAMEMIGCC", "shape_box", "shape_sphere", "KJPMLHHAPJE", "CCACOJPKPOH", "APICIBIFLAK", "EDBFACBGBCE", "LFCJFGOIEEK", "KDEMGBKBOMA")
    BJDAMEMIGCC_FIELD_NUMBER: _ClassVar[int]
    SHAPE_BOX_FIELD_NUMBER: _ClassVar[int]
    SHAPE_SPHERE_FIELD_NUMBER: _ClassVar[int]
    KJPMLHHAPJE_FIELD_NUMBER: _ClassVar[int]
    CCACOJPKPOH_FIELD_NUMBER: _ClassVar[int]
    APICIBIFLAK_FIELD_NUMBER: _ClassVar[int]
    EDBFACBGBCE_FIELD_NUMBER: _ClassVar[int]
    LFCJFGOIEEK_FIELD_NUMBER: _ClassVar[int]
    KDEMGBKBOMA_FIELD_NUMBER: _ClassVar[int]
    BJDAMEMIGCC: int
    shape_box: _PHDAEEHJBBA_pb2.PHDAEEHJBBA
    shape_sphere: _GFINLGDCIIN_pb2.GFINLGDCIIN
    KJPMLHHAPJE: float
    CCACOJPKPOH: int
    APICIBIFLAK: int
    EDBFACBGBCE: int
    LFCJFGOIEEK: int
    KDEMGBKBOMA: int
    def __init__(self, BJDAMEMIGCC: _Optional[int] = ..., shape_box: _Optional[_Union[_PHDAEEHJBBA_pb2.PHDAEEHJBBA, _Mapping]] = ..., shape_sphere: _Optional[_Union[_GFINLGDCIIN_pb2.GFINLGDCIIN, _Mapping]] = ..., KJPMLHHAPJE: _Optional[float] = ..., CCACOJPKPOH: _Optional[int] = ..., APICIBIFLAK: _Optional[int] = ..., EDBFACBGBCE: _Optional[int] = ..., LFCJFGOIEEK: _Optional[int] = ..., KDEMGBKBOMA: _Optional[int] = ...) -> None: ...
