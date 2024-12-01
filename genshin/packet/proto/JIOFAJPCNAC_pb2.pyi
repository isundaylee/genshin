from genshin.packet.proto import PCPKMBJDJAK_pb2 as _PCPKMBJDJAK_pb2
from genshin.packet.proto import IACMANPJHJI_pb2 as _IACMANPJHJI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JIOFAJPCNAC(_message.Message):
    __slots__ = ("GAAKALGOBCF", "EJNINFFFKJP", "GHLBJAHJEHF", "DDJFGLFNGJC", "OCKIBANLDMK", "KGCONLDGJPG")
    GAAKALGOBCF_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GHLBJAHJEHF_FIELD_NUMBER: _ClassVar[int]
    DDJFGLFNGJC_FIELD_NUMBER: _ClassVar[int]
    OCKIBANLDMK_FIELD_NUMBER: _ClassVar[int]
    KGCONLDGJPG_FIELD_NUMBER: _ClassVar[int]
    GAAKALGOBCF: _PCPKMBJDJAK_pb2.PCPKMBJDJAK
    EJNINFFFKJP: int
    GHLBJAHJEHF: int
    DDJFGLFNGJC: int
    OCKIBANLDMK: int
    KGCONLDGJPG: _IACMANPJHJI_pb2.IACMANPJHJI
    def __init__(self, GAAKALGOBCF: _Optional[_Union[_PCPKMBJDJAK_pb2.PCPKMBJDJAK, str]] = ..., EJNINFFFKJP: _Optional[int] = ..., GHLBJAHJEHF: _Optional[int] = ..., DDJFGLFNGJC: _Optional[int] = ..., OCKIBANLDMK: _Optional[int] = ..., KGCONLDGJPG: _Optional[_Union[_IACMANPJHJI_pb2.IACMANPJHJI, str]] = ...) -> None: ...
