from genshin.packet.proto import OLHEKLKENDN_pb2 as _OLHEKLKENDN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MINGHCPOBNG(_message.Message):
    __slots__ = ("FGAEINCCKDK", "JIANNPFIHHB", "NCCPPHNNPBF", "HJJFOKHFNKO", "FJAMCDJDJOA", "LGFKALAMILP")
    class JIANNPFIHHBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FGAEINCCKDK_FIELD_NUMBER: _ClassVar[int]
    JIANNPFIHHB_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    HJJFOKHFNKO_FIELD_NUMBER: _ClassVar[int]
    FJAMCDJDJOA_FIELD_NUMBER: _ClassVar[int]
    LGFKALAMILP_FIELD_NUMBER: _ClassVar[int]
    FGAEINCCKDK: _OLHEKLKENDN_pb2.OLHEKLKENDN
    JIANNPFIHHB: _containers.ScalarMap[int, int]
    NCCPPHNNPBF: int
    HJJFOKHFNKO: int
    FJAMCDJDJOA: int
    LGFKALAMILP: int
    def __init__(self, FGAEINCCKDK: _Optional[_Union[_OLHEKLKENDN_pb2.OLHEKLKENDN, _Mapping]] = ..., JIANNPFIHHB: _Optional[_Mapping[int, int]] = ..., NCCPPHNNPBF: _Optional[int] = ..., HJJFOKHFNKO: _Optional[int] = ..., FJAMCDJDJOA: _Optional[int] = ..., LGFKALAMILP: _Optional[int] = ...) -> None: ...
