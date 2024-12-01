from genshin.packet.proto import MCIGBDLJIFH_pb2 as _MCIGBDLJIFH_pb2
from genshin.packet.proto import AGEFELGNKLA_pb2 as _AGEFELGNKLA_pb2
from genshin.packet.proto import FMPAGIFCMLJ_pb2 as _FMPAGIFCMLJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JOCLMPHLJBB(_message.Message):
    __slots__ = ("KCKEPCMLIHI", "GOLEMMJGIJL", "LIPECKNCEII", "LMFECBHLMBD")
    KCKEPCMLIHI_FIELD_NUMBER: _ClassVar[int]
    GOLEMMJGIJL_FIELD_NUMBER: _ClassVar[int]
    LIPECKNCEII_FIELD_NUMBER: _ClassVar[int]
    LMFECBHLMBD_FIELD_NUMBER: _ClassVar[int]
    KCKEPCMLIHI: _containers.RepeatedCompositeFieldContainer[_MCIGBDLJIFH_pb2.MCIGBDLJIFH]
    GOLEMMJGIJL: _AGEFELGNKLA_pb2.AGEFELGNKLA
    LIPECKNCEII: _FMPAGIFCMLJ_pb2.FMPAGIFCMLJ
    LMFECBHLMBD: int
    def __init__(self, KCKEPCMLIHI: _Optional[_Iterable[_Union[_MCIGBDLJIFH_pb2.MCIGBDLJIFH, _Mapping]]] = ..., GOLEMMJGIJL: _Optional[_Union[_AGEFELGNKLA_pb2.AGEFELGNKLA, _Mapping]] = ..., LIPECKNCEII: _Optional[_Union[_FMPAGIFCMLJ_pb2.FMPAGIFCMLJ, _Mapping]] = ..., LMFECBHLMBD: _Optional[int] = ...) -> None: ...
