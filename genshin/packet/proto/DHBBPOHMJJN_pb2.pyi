from genshin.packet.proto import AINAHDONFEO_pb2 as _AINAHDONFEO_pb2
from genshin.packet.proto import AIPIIHKMOGO_pb2 as _AIPIIHKMOGO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DHBBPOHMJJN(_message.Message):
    __slots__ = ("MDCJIJLNKHL", "FBFDAKLPEFB", "BLHDMDOKALP")
    MDCJIJLNKHL_FIELD_NUMBER: _ClassVar[int]
    FBFDAKLPEFB_FIELD_NUMBER: _ClassVar[int]
    BLHDMDOKALP_FIELD_NUMBER: _ClassVar[int]
    MDCJIJLNKHL: _containers.RepeatedScalarFieldContainer[int]
    FBFDAKLPEFB: _AINAHDONFEO_pb2.AINAHDONFEO
    BLHDMDOKALP: _AIPIIHKMOGO_pb2.AIPIIHKMOGO
    def __init__(self, MDCJIJLNKHL: _Optional[_Iterable[int]] = ..., FBFDAKLPEFB: _Optional[_Union[_AINAHDONFEO_pb2.AINAHDONFEO, str]] = ..., BLHDMDOKALP: _Optional[_Union[_AIPIIHKMOGO_pb2.AIPIIHKMOGO, str]] = ...) -> None: ...
