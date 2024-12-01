from genshin.packet.proto import HKHGFIHOKNC_pb2 as _HKHGFIHOKNC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FAPGMOOJHEI(_message.Message):
    __slots__ = ("EMFHFEGCJJB", "EJNINFFFKJP", "HNJJLAANFLG", "ILNBDDPAKHP")
    EMFHFEGCJJB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    HNJJLAANFLG_FIELD_NUMBER: _ClassVar[int]
    ILNBDDPAKHP_FIELD_NUMBER: _ClassVar[int]
    EMFHFEGCJJB: _containers.RepeatedCompositeFieldContainer[_HKHGFIHOKNC_pb2.HKHGFIHOKNC]
    EJNINFFFKJP: int
    HNJJLAANFLG: bool
    ILNBDDPAKHP: bool
    def __init__(self, EMFHFEGCJJB: _Optional[_Iterable[_Union[_HKHGFIHOKNC_pb2.HKHGFIHOKNC, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., HNJJLAANFLG: bool = ..., ILNBDDPAKHP: bool = ...) -> None: ...
