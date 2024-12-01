from genshin.packet.proto import HLBNLHGCPFC_pb2 as _HLBNLHGCPFC_pb2
from genshin.packet.proto import JDEHFAEIDON_pb2 as _JDEHFAEIDON_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AEFLPKAEJDE(_message.Message):
    __slots__ = ("FGEFHBEPFAA", "LEBKPFCAKFL", "PJLONIBLAAE", "HDBCHCEMAJC", "MPFLDFDOGAI")
    FGEFHBEPFAA_FIELD_NUMBER: _ClassVar[int]
    LEBKPFCAKFL_FIELD_NUMBER: _ClassVar[int]
    PJLONIBLAAE_FIELD_NUMBER: _ClassVar[int]
    HDBCHCEMAJC_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    FGEFHBEPFAA: _containers.RepeatedCompositeFieldContainer[_HLBNLHGCPFC_pb2.HLBNLHGCPFC]
    LEBKPFCAKFL: _containers.RepeatedCompositeFieldContainer[_JDEHFAEIDON_pb2.JDEHFAEIDON]
    PJLONIBLAAE: int
    HDBCHCEMAJC: int
    MPFLDFDOGAI: bool
    def __init__(self, FGEFHBEPFAA: _Optional[_Iterable[_Union[_HLBNLHGCPFC_pb2.HLBNLHGCPFC, _Mapping]]] = ..., LEBKPFCAKFL: _Optional[_Iterable[_Union[_JDEHFAEIDON_pb2.JDEHFAEIDON, _Mapping]]] = ..., PJLONIBLAAE: _Optional[int] = ..., HDBCHCEMAJC: _Optional[int] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
