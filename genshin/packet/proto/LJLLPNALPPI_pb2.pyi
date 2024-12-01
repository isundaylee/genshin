from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import IACMANPJHJI_pb2 as _IACMANPJHJI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LJLLPNALPPI(_message.Message):
    __slots__ = ("BNJOJBOPMFJ", "NJCAFAAGMJK", "GHLBJAHJEHF", "OCKIBANLDMK", "KGCONLDGJPG")
    BNJOJBOPMFJ_FIELD_NUMBER: _ClassVar[int]
    NJCAFAAGMJK_FIELD_NUMBER: _ClassVar[int]
    GHLBJAHJEHF_FIELD_NUMBER: _ClassVar[int]
    OCKIBANLDMK_FIELD_NUMBER: _ClassVar[int]
    KGCONLDGJPG_FIELD_NUMBER: _ClassVar[int]
    BNJOJBOPMFJ: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    NJCAFAAGMJK: _containers.RepeatedScalarFieldContainer[int]
    GHLBJAHJEHF: int
    OCKIBANLDMK: int
    KGCONLDGJPG: _IACMANPJHJI_pb2.IACMANPJHJI
    def __init__(self, BNJOJBOPMFJ: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., NJCAFAAGMJK: _Optional[_Iterable[int]] = ..., GHLBJAHJEHF: _Optional[int] = ..., OCKIBANLDMK: _Optional[int] = ..., KGCONLDGJPG: _Optional[_Union[_IACMANPJHJI_pb2.IACMANPJHJI, str]] = ...) -> None: ...
