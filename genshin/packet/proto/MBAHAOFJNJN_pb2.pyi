from genshin.packet.proto import LKOFCBNNOAM_pb2 as _LKOFCBNNOAM_pb2
from genshin.packet.proto import AIPIIHKMOGO_pb2 as _AIPIIHKMOGO_pb2
from genshin.packet.proto import AINAHDONFEO_pb2 as _AINAHDONFEO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MBAHAOFJNJN(_message.Message):
    __slots__ = ("KGFPCMBDPAJ", "MDCJIJLNKHL", "BLHDMDOKALP", "FBFDAKLPEFB")
    KGFPCMBDPAJ_FIELD_NUMBER: _ClassVar[int]
    MDCJIJLNKHL_FIELD_NUMBER: _ClassVar[int]
    BLHDMDOKALP_FIELD_NUMBER: _ClassVar[int]
    FBFDAKLPEFB_FIELD_NUMBER: _ClassVar[int]
    KGFPCMBDPAJ: _LKOFCBNNOAM_pb2.LKOFCBNNOAM
    MDCJIJLNKHL: _containers.RepeatedScalarFieldContainer[int]
    BLHDMDOKALP: _AIPIIHKMOGO_pb2.AIPIIHKMOGO
    FBFDAKLPEFB: _AINAHDONFEO_pb2.AINAHDONFEO
    def __init__(self, KGFPCMBDPAJ: _Optional[_Union[_LKOFCBNNOAM_pb2.LKOFCBNNOAM, _Mapping]] = ..., MDCJIJLNKHL: _Optional[_Iterable[int]] = ..., BLHDMDOKALP: _Optional[_Union[_AIPIIHKMOGO_pb2.AIPIIHKMOGO, str]] = ..., FBFDAKLPEFB: _Optional[_Union[_AINAHDONFEO_pb2.AINAHDONFEO, str]] = ...) -> None: ...
