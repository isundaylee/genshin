from genshin.packet.proto import DKIFDGNKPLD_pb2 as _DKIFDGNKPLD_pb2
from genshin.packet.proto import APMHHCOHPLD_pb2 as _APMHHCOHPLD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGGELDLHDAJ(_message.Message):
    __slots__ = ("CIENOKDHFOD", "KGOJIPMFHBM", "GDJKCKNOGBD", "IGBDOEBPPHO", "is_locked")
    CIENOKDHFOD_FIELD_NUMBER: _ClassVar[int]
    KGOJIPMFHBM_FIELD_NUMBER: _ClassVar[int]
    GDJKCKNOGBD_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    CIENOKDHFOD: _DKIFDGNKPLD_pb2.DKIFDGNKPLD
    KGOJIPMFHBM: _containers.RepeatedScalarFieldContainer[int]
    GDJKCKNOGBD: _APMHHCOHPLD_pb2.APMHHCOHPLD
    IGBDOEBPPHO: int
    is_locked: bool
    def __init__(self, CIENOKDHFOD: _Optional[_Union[_DKIFDGNKPLD_pb2.DKIFDGNKPLD, _Mapping]] = ..., KGOJIPMFHBM: _Optional[_Iterable[int]] = ..., GDJKCKNOGBD: _Optional[_Union[_APMHHCOHPLD_pb2.APMHHCOHPLD, _Mapping]] = ..., IGBDOEBPPHO: _Optional[int] = ..., is_locked: bool = ...) -> None: ...
