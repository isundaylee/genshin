from genshin.packet.proto import APMHHCOHPLD_pb2 as _APMHHCOHPLD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OKNBFFIFIGJ(_message.Message):
    __slots__ = ("KGOJIPMFHBM", "GDJKCKNOGBD", "DLGFBKCFFAO")
    KGOJIPMFHBM_FIELD_NUMBER: _ClassVar[int]
    GDJKCKNOGBD_FIELD_NUMBER: _ClassVar[int]
    DLGFBKCFFAO_FIELD_NUMBER: _ClassVar[int]
    KGOJIPMFHBM: _containers.RepeatedScalarFieldContainer[int]
    GDJKCKNOGBD: _APMHHCOHPLD_pb2.APMHHCOHPLD
    DLGFBKCFFAO: int
    def __init__(self, KGOJIPMFHBM: _Optional[_Iterable[int]] = ..., GDJKCKNOGBD: _Optional[_Union[_APMHHCOHPLD_pb2.APMHHCOHPLD, _Mapping]] = ..., DLGFBKCFFAO: _Optional[int] = ...) -> None: ...
