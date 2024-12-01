from genshin.packet.proto import IACMANPJHJI_pb2 as _IACMANPJHJI_pb2
from genshin.packet.proto import IEBMAHKGIPD_pb2 as _IEBMAHKGIPD_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KIKLGFAPPMG(_message.Message):
    __slots__ = ("CKLJMDGLIHF", "MOFIPIHBEKB", "GHLBJAHJEHF", "KGCONLDGJPG", "OCKIBANLDMK", "HKBDFPJIOLC", "DDJFGLFNGJC")
    CKLJMDGLIHF_FIELD_NUMBER: _ClassVar[int]
    MOFIPIHBEKB_FIELD_NUMBER: _ClassVar[int]
    GHLBJAHJEHF_FIELD_NUMBER: _ClassVar[int]
    KGCONLDGJPG_FIELD_NUMBER: _ClassVar[int]
    OCKIBANLDMK_FIELD_NUMBER: _ClassVar[int]
    HKBDFPJIOLC_FIELD_NUMBER: _ClassVar[int]
    DDJFGLFNGJC_FIELD_NUMBER: _ClassVar[int]
    CKLJMDGLIHF: bool
    MOFIPIHBEKB: int
    GHLBJAHJEHF: int
    KGCONLDGJPG: _IACMANPJHJI_pb2.IACMANPJHJI
    OCKIBANLDMK: int
    HKBDFPJIOLC: _IEBMAHKGIPD_pb2.IEBMAHKGIPD
    DDJFGLFNGJC: int
    def __init__(self, CKLJMDGLIHF: bool = ..., MOFIPIHBEKB: _Optional[int] = ..., GHLBJAHJEHF: _Optional[int] = ..., KGCONLDGJPG: _Optional[_Union[_IACMANPJHJI_pb2.IACMANPJHJI, str]] = ..., OCKIBANLDMK: _Optional[int] = ..., HKBDFPJIOLC: _Optional[_Union[_IEBMAHKGIPD_pb2.IEBMAHKGIPD, str]] = ..., DDJFGLFNGJC: _Optional[int] = ...) -> None: ...
