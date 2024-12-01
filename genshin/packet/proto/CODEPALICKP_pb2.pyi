from genshin.packet.proto import PCPKMBJDJAK_pb2 as _PCPKMBJDJAK_pb2
from genshin.packet.proto import IACMANPJHJI_pb2 as _IACMANPJHJI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CODEPALICKP(_message.Message):
    __slots__ = ("EJNINFFFKJP", "GAAKALGOBCF", "GHLBJAHJEHF", "KGCONLDGJPG", "OCKIBANLDMK")
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GAAKALGOBCF_FIELD_NUMBER: _ClassVar[int]
    GHLBJAHJEHF_FIELD_NUMBER: _ClassVar[int]
    KGCONLDGJPG_FIELD_NUMBER: _ClassVar[int]
    OCKIBANLDMK_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP: int
    GAAKALGOBCF: _PCPKMBJDJAK_pb2.PCPKMBJDJAK
    GHLBJAHJEHF: int
    KGCONLDGJPG: _IACMANPJHJI_pb2.IACMANPJHJI
    OCKIBANLDMK: int
    def __init__(self, EJNINFFFKJP: _Optional[int] = ..., GAAKALGOBCF: _Optional[_Union[_PCPKMBJDJAK_pb2.PCPKMBJDJAK, str]] = ..., GHLBJAHJEHF: _Optional[int] = ..., KGCONLDGJPG: _Optional[_Union[_IACMANPJHJI_pb2.IACMANPJHJI, str]] = ..., OCKIBANLDMK: _Optional[int] = ...) -> None: ...
