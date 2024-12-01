from genshin.packet.proto import FJCOKOHBJIN_pb2 as _FJCOKOHBJIN_pb2
from genshin.packet.proto import IMGPEMFGOPF_pb2 as _IMGPEMFGOPF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DJFGBOGDMLE(_message.Message):
    __slots__ = ("BCKBKIDDFCD", "OHMKBGAMEIM", "MPPCKLOHOAD", "COKCGKDPPEM", "JMJDHNPAKEI", "MEJLFKPFPGK", "life_state", "HFEBJEFKLHN")
    BCKBKIDDFCD_FIELD_NUMBER: _ClassVar[int]
    OHMKBGAMEIM_FIELD_NUMBER: _ClassVar[int]
    MPPCKLOHOAD_FIELD_NUMBER: _ClassVar[int]
    COKCGKDPPEM_FIELD_NUMBER: _ClassVar[int]
    JMJDHNPAKEI_FIELD_NUMBER: _ClassVar[int]
    MEJLFKPFPGK_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    HFEBJEFKLHN_FIELD_NUMBER: _ClassVar[int]
    BCKBKIDDFCD: _containers.RepeatedCompositeFieldContainer[_FJCOKOHBJIN_pb2.FJCOKOHBJIN]
    OHMKBGAMEIM: _containers.RepeatedScalarFieldContainer[str]
    MPPCKLOHOAD: str
    COKCGKDPPEM: _IMGPEMFGOPF_pb2.IMGPEMFGOPF
    JMJDHNPAKEI: int
    MEJLFKPFPGK: int
    life_state: int
    HFEBJEFKLHN: int
    def __init__(self, BCKBKIDDFCD: _Optional[_Iterable[_Union[_FJCOKOHBJIN_pb2.FJCOKOHBJIN, _Mapping]]] = ..., OHMKBGAMEIM: _Optional[_Iterable[str]] = ..., MPPCKLOHOAD: _Optional[str] = ..., COKCGKDPPEM: _Optional[_Union[_IMGPEMFGOPF_pb2.IMGPEMFGOPF, str]] = ..., JMJDHNPAKEI: _Optional[int] = ..., MEJLFKPFPGK: _Optional[int] = ..., life_state: _Optional[int] = ..., HFEBJEFKLHN: _Optional[int] = ...) -> None: ...
