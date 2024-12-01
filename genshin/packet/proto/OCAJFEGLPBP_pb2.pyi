from genshin.packet.proto import GBGADBFFGOO_pb2 as _GBGADBFFGOO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OCAJFEGLPBP(_message.Message):
    __slots__ = ("KCDEGDMLKCB", "AMHHLEOKOKB", "HBCNMJBFOOO", "BDDOKMIEJPH", "EJNINFFFKJP", "EPJGHNLEIOO", "OKIMGMGPGPG")
    KCDEGDMLKCB_FIELD_NUMBER: _ClassVar[int]
    AMHHLEOKOKB_FIELD_NUMBER: _ClassVar[int]
    HBCNMJBFOOO_FIELD_NUMBER: _ClassVar[int]
    BDDOKMIEJPH_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    EPJGHNLEIOO_FIELD_NUMBER: _ClassVar[int]
    OKIMGMGPGPG_FIELD_NUMBER: _ClassVar[int]
    KCDEGDMLKCB: _containers.RepeatedScalarFieldContainer[int]
    AMHHLEOKOKB: _containers.RepeatedScalarFieldContainer[int]
    HBCNMJBFOOO: _containers.RepeatedScalarFieldContainer[int]
    BDDOKMIEJPH: _containers.RepeatedCompositeFieldContainer[_GBGADBFFGOO_pb2.GBGADBFFGOO]
    EJNINFFFKJP: int
    EPJGHNLEIOO: int
    OKIMGMGPGPG: int
    def __init__(self, KCDEGDMLKCB: _Optional[_Iterable[int]] = ..., AMHHLEOKOKB: _Optional[_Iterable[int]] = ..., HBCNMJBFOOO: _Optional[_Iterable[int]] = ..., BDDOKMIEJPH: _Optional[_Iterable[_Union[_GBGADBFFGOO_pb2.GBGADBFFGOO, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., EPJGHNLEIOO: _Optional[int] = ..., OKIMGMGPGPG: _Optional[int] = ...) -> None: ...
