from genshin.packet.proto import MKKMACFGJBG_pb2 as _MKKMACFGJBG_pb2
from genshin.packet.proto import MKDHKGKNKBO_pb2 as _MKDHKGKNKBO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JIGGIIPGFPI(_message.Message):
    __slots__ = ("LPKDBFNIJDA", "KBJBNEJOBNM", "EHAEACFBOOL", "NFICKLLNFGN", "EJNINFFFKJP")
    LPKDBFNIJDA_FIELD_NUMBER: _ClassVar[int]
    KBJBNEJOBNM_FIELD_NUMBER: _ClassVar[int]
    EHAEACFBOOL_FIELD_NUMBER: _ClassVar[int]
    NFICKLLNFGN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    LPKDBFNIJDA: _containers.RepeatedCompositeFieldContainer[_MKKMACFGJBG_pb2.MKKMACFGJBG]
    KBJBNEJOBNM: _MKDHKGKNKBO_pb2.MKDHKGKNKBO
    EHAEACFBOOL: int
    NFICKLLNFGN: int
    EJNINFFFKJP: int
    def __init__(self, LPKDBFNIJDA: _Optional[_Iterable[_Union[_MKKMACFGJBG_pb2.MKKMACFGJBG, _Mapping]]] = ..., KBJBNEJOBNM: _Optional[_Union[_MKDHKGKNKBO_pb2.MKDHKGKNKBO, _Mapping]] = ..., EHAEACFBOOL: _Optional[int] = ..., NFICKLLNFGN: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
