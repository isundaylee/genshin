from genshin.packet.proto import ACEKDEBFIMC_pb2 as _ACEKDEBFIMC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CHNDGMMBKDI(_message.Message):
    __slots__ = ("NFMBFOGNCNL", "HGGJIHMNEBA", "CDFIKAPILPF", "MNCBKGJGGLL")
    NFMBFOGNCNL_FIELD_NUMBER: _ClassVar[int]
    HGGJIHMNEBA_FIELD_NUMBER: _ClassVar[int]
    CDFIKAPILPF_FIELD_NUMBER: _ClassVar[int]
    MNCBKGJGGLL_FIELD_NUMBER: _ClassVar[int]
    NFMBFOGNCNL: _containers.RepeatedCompositeFieldContainer[_ACEKDEBFIMC_pb2.ACEKDEBFIMC]
    HGGJIHMNEBA: _containers.RepeatedScalarFieldContainer[int]
    CDFIKAPILPF: int
    MNCBKGJGGLL: int
    def __init__(self, NFMBFOGNCNL: _Optional[_Iterable[_Union[_ACEKDEBFIMC_pb2.ACEKDEBFIMC, _Mapping]]] = ..., HGGJIHMNEBA: _Optional[_Iterable[int]] = ..., CDFIKAPILPF: _Optional[int] = ..., MNCBKGJGGLL: _Optional[int] = ...) -> None: ...
