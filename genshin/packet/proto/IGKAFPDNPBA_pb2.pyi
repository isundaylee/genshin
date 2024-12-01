from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import PACJKIOLAOH_pb2 as _PACJKIOLAOH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IGKAFPDNPBA(_message.Message):
    __slots__ = ("HPOECKEKAFA", "CCKJPDCHOBJ", "IGBDOEBPPHO", "LAILPNOOAJC", "IDPELOPJNKE", "FFOBIONLMOJ", "KJDMOOFKNEK", "BBAFIOKGDBN")
    HPOECKEKAFA_FIELD_NUMBER: _ClassVar[int]
    CCKJPDCHOBJ_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    LAILPNOOAJC_FIELD_NUMBER: _ClassVar[int]
    IDPELOPJNKE_FIELD_NUMBER: _ClassVar[int]
    FFOBIONLMOJ_FIELD_NUMBER: _ClassVar[int]
    KJDMOOFKNEK_FIELD_NUMBER: _ClassVar[int]
    BBAFIOKGDBN_FIELD_NUMBER: _ClassVar[int]
    HPOECKEKAFA: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    CCKJPDCHOBJ: int
    IGBDOEBPPHO: int
    LAILPNOOAJC: bool
    IDPELOPJNKE: bool
    FFOBIONLMOJ: int
    KJDMOOFKNEK: int
    BBAFIOKGDBN: _PACJKIOLAOH_pb2.PACJKIOLAOH
    def __init__(self, HPOECKEKAFA: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., CCKJPDCHOBJ: _Optional[int] = ..., IGBDOEBPPHO: _Optional[int] = ..., LAILPNOOAJC: bool = ..., IDPELOPJNKE: bool = ..., FFOBIONLMOJ: _Optional[int] = ..., KJDMOOFKNEK: _Optional[int] = ..., BBAFIOKGDBN: _Optional[_Union[_PACJKIOLAOH_pb2.PACJKIOLAOH, str]] = ...) -> None: ...
