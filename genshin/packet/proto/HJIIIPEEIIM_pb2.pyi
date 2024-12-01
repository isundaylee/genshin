from genshin.packet.proto import IBDNAOGMOFO_pb2 as _IBDNAOGMOFO_pb2
from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HJIIIPEEIIM(_message.Message):
    __slots__ = ("CMIIEGLHFFL", "DGHLOIEEMCG", "IEJJAFIBEFP", "GANAOAINDNG", "LOJPODLLAIF", "IBHDPGMKHHN", "PIEAPGEPMLF", "LAILPNOOAJC")
    CMIIEGLHFFL_FIELD_NUMBER: _ClassVar[int]
    DGHLOIEEMCG_FIELD_NUMBER: _ClassVar[int]
    IEJJAFIBEFP_FIELD_NUMBER: _ClassVar[int]
    GANAOAINDNG_FIELD_NUMBER: _ClassVar[int]
    LOJPODLLAIF_FIELD_NUMBER: _ClassVar[int]
    IBHDPGMKHHN_FIELD_NUMBER: _ClassVar[int]
    PIEAPGEPMLF_FIELD_NUMBER: _ClassVar[int]
    LAILPNOOAJC_FIELD_NUMBER: _ClassVar[int]
    CMIIEGLHFFL: _containers.RepeatedScalarFieldContainer[int]
    DGHLOIEEMCG: _containers.RepeatedCompositeFieldContainer[_IBDNAOGMOFO_pb2.IBDNAOGMOFO]
    IEJJAFIBEFP: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    GANAOAINDNG: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    LOJPODLLAIF: int
    IBHDPGMKHHN: int
    PIEAPGEPMLF: int
    LAILPNOOAJC: bool
    def __init__(self, CMIIEGLHFFL: _Optional[_Iterable[int]] = ..., DGHLOIEEMCG: _Optional[_Iterable[_Union[_IBDNAOGMOFO_pb2.IBDNAOGMOFO, _Mapping]]] = ..., IEJJAFIBEFP: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., GANAOAINDNG: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., LOJPODLLAIF: _Optional[int] = ..., IBHDPGMKHHN: _Optional[int] = ..., PIEAPGEPMLF: _Optional[int] = ..., LAILPNOOAJC: bool = ...) -> None: ...
