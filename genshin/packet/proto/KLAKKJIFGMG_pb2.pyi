from genshin.packet.proto import FIJDALPGDCN_pb2 as _FIJDALPGDCN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KLAKKJIFGMG(_message.Message):
    __slots__ = ("GJDPCOOMAJK", "ACPHEGPGPOH", "COOKMNEFHKF", "IGBDOEBPPHO")
    GJDPCOOMAJK_FIELD_NUMBER: _ClassVar[int]
    ACPHEGPGPOH_FIELD_NUMBER: _ClassVar[int]
    COOKMNEFHKF_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    GJDPCOOMAJK: _containers.RepeatedCompositeFieldContainer[_FIJDALPGDCN_pb2.FIJDALPGDCN]
    ACPHEGPGPOH: _containers.RepeatedScalarFieldContainer[int]
    COOKMNEFHKF: bool
    IGBDOEBPPHO: int
    def __init__(self, GJDPCOOMAJK: _Optional[_Iterable[_Union[_FIJDALPGDCN_pb2.FIJDALPGDCN, _Mapping]]] = ..., ACPHEGPGPOH: _Optional[_Iterable[int]] = ..., COOKMNEFHKF: bool = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
