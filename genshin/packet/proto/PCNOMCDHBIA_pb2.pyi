from genshin.packet.proto import MKJGCFHIIHN_pb2 as _MKJGCFHIIHN_pb2
from genshin.packet.proto import GJJCHDFDJPL_pb2 as _GJJCHDFDJPL_pb2
from genshin.packet.proto import KICDEFNONLA_pb2 as _KICDEFNONLA_pb2
from genshin.packet.proto import PHGGEOPNMBP_pb2 as _PHGGEOPNMBP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCNOMCDHBIA(_message.Message):
    __slots__ = ("BFMMHKFPCJB", "HNLJPNMJPIC", "GLCIAEKDPGL", "countdown", "timer", "normal", "NKNKFMJMFND", "IADFGKJCIDE")
    BFMMHKFPCJB_FIELD_NUMBER: _ClassVar[int]
    HNLJPNMJPIC_FIELD_NUMBER: _ClassVar[int]
    GLCIAEKDPGL_FIELD_NUMBER: _ClassVar[int]
    COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
    TIMER_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    NKNKFMJMFND_FIELD_NUMBER: _ClassVar[int]
    IADFGKJCIDE_FIELD_NUMBER: _ClassVar[int]
    BFMMHKFPCJB: str
    HNLJPNMJPIC: _containers.RepeatedScalarFieldContainer[int]
    GLCIAEKDPGL: int
    countdown: _MKJGCFHIIHN_pb2.MKJGCFHIIHN
    timer: _GJJCHDFDJPL_pb2.GJJCHDFDJPL
    normal: _KICDEFNONLA_pb2.KICDEFNONLA
    NKNKFMJMFND: int
    IADFGKJCIDE: _PHGGEOPNMBP_pb2.PHGGEOPNMBP
    def __init__(self, BFMMHKFPCJB: _Optional[str] = ..., HNLJPNMJPIC: _Optional[_Iterable[int]] = ..., GLCIAEKDPGL: _Optional[int] = ..., countdown: _Optional[_Union[_MKJGCFHIIHN_pb2.MKJGCFHIIHN, _Mapping]] = ..., timer: _Optional[_Union[_GJJCHDFDJPL_pb2.GJJCHDFDJPL, _Mapping]] = ..., normal: _Optional[_Union[_KICDEFNONLA_pb2.KICDEFNONLA, _Mapping]] = ..., NKNKFMJMFND: _Optional[int] = ..., IADFGKJCIDE: _Optional[_Union[_PHGGEOPNMBP_pb2.PHGGEOPNMBP, str]] = ...) -> None: ...
