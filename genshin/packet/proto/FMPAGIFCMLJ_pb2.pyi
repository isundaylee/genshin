from genshin.packet.proto import BODFNFIDFOD_pb2 as _BODFNFIDFOD_pb2
from genshin.packet.proto import BGPAHBMKBAG_pb2 as _BGPAHBMKBAG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FMPAGIFCMLJ(_message.Message):
    __slots__ = ("NPMIAGMNMAN", "ICFGKPFAFND", "MJAONINHIIB", "IFIPFMLJPGC")
    NPMIAGMNMAN_FIELD_NUMBER: _ClassVar[int]
    ICFGKPFAFND_FIELD_NUMBER: _ClassVar[int]
    MJAONINHIIB_FIELD_NUMBER: _ClassVar[int]
    IFIPFMLJPGC_FIELD_NUMBER: _ClassVar[int]
    NPMIAGMNMAN: _BODFNFIDFOD_pb2.BODFNFIDFOD
    ICFGKPFAFND: _BODFNFIDFOD_pb2.BODFNFIDFOD
    MJAONINHIIB: _containers.RepeatedScalarFieldContainer[int]
    IFIPFMLJPGC: _containers.RepeatedCompositeFieldContainer[_BGPAHBMKBAG_pb2.BGPAHBMKBAG]
    def __init__(self, NPMIAGMNMAN: _Optional[_Union[_BODFNFIDFOD_pb2.BODFNFIDFOD, _Mapping]] = ..., ICFGKPFAFND: _Optional[_Union[_BODFNFIDFOD_pb2.BODFNFIDFOD, _Mapping]] = ..., MJAONINHIIB: _Optional[_Iterable[int]] = ..., IFIPFMLJPGC: _Optional[_Iterable[_Union[_BGPAHBMKBAG_pb2.BGPAHBMKBAG, _Mapping]]] = ...) -> None: ...
