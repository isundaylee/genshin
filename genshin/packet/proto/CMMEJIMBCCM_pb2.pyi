from genshin.packet.proto import FJCOKOHBJIN_pb2 as _FJCOKOHBJIN_pb2
from genshin.packet.proto import IMGPEMFGOPF_pb2 as _IMGPEMFGOPF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMMEJIMBCCM(_message.Message):
    __slots__ = ("OHMKBGAMEIM", "BCKBKIDDFCD", "MPPCKLOHOAD", "AGIDBEEINDE", "JMJDHNPAKEI", "life_state", "COKCGKDPPEM", "HFEBJEFKLHN")
    OHMKBGAMEIM_FIELD_NUMBER: _ClassVar[int]
    BCKBKIDDFCD_FIELD_NUMBER: _ClassVar[int]
    MPPCKLOHOAD_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    JMJDHNPAKEI_FIELD_NUMBER: _ClassVar[int]
    LIFE_STATE_FIELD_NUMBER: _ClassVar[int]
    COKCGKDPPEM_FIELD_NUMBER: _ClassVar[int]
    HFEBJEFKLHN_FIELD_NUMBER: _ClassVar[int]
    OHMKBGAMEIM: _containers.RepeatedScalarFieldContainer[str]
    BCKBKIDDFCD: _containers.RepeatedCompositeFieldContainer[_FJCOKOHBJIN_pb2.FJCOKOHBJIN]
    MPPCKLOHOAD: str
    AGIDBEEINDE: int
    JMJDHNPAKEI: int
    life_state: int
    COKCGKDPPEM: _IMGPEMFGOPF_pb2.IMGPEMFGOPF
    HFEBJEFKLHN: int
    def __init__(self, OHMKBGAMEIM: _Optional[_Iterable[str]] = ..., BCKBKIDDFCD: _Optional[_Iterable[_Union[_FJCOKOHBJIN_pb2.FJCOKOHBJIN, _Mapping]]] = ..., MPPCKLOHOAD: _Optional[str] = ..., AGIDBEEINDE: _Optional[int] = ..., JMJDHNPAKEI: _Optional[int] = ..., life_state: _Optional[int] = ..., COKCGKDPPEM: _Optional[_Union[_IMGPEMFGOPF_pb2.IMGPEMFGOPF, str]] = ..., HFEBJEFKLHN: _Optional[int] = ...) -> None: ...
