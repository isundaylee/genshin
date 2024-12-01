from genshin.packet.proto import LKOFCBNNOAM_pb2 as _LKOFCBNNOAM_pb2
from genshin.packet.proto import AINAHDONFEO_pb2 as _AINAHDONFEO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HHOMBFNBGPG(_message.Message):
    __slots__ = ("KGFPCMBDPAJ", "KNCCAOOGNEE", "FBFDAKLPEFB", "EJNINFFFKJP")
    class KNCCAOOGNEEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    KGFPCMBDPAJ_FIELD_NUMBER: _ClassVar[int]
    KNCCAOOGNEE_FIELD_NUMBER: _ClassVar[int]
    FBFDAKLPEFB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    KGFPCMBDPAJ: _LKOFCBNNOAM_pb2.LKOFCBNNOAM
    KNCCAOOGNEE: _containers.ScalarMap[int, int]
    FBFDAKLPEFB: _AINAHDONFEO_pb2.AINAHDONFEO
    EJNINFFFKJP: int
    def __init__(self, KGFPCMBDPAJ: _Optional[_Union[_LKOFCBNNOAM_pb2.LKOFCBNNOAM, _Mapping]] = ..., KNCCAOOGNEE: _Optional[_Mapping[int, int]] = ..., FBFDAKLPEFB: _Optional[_Union[_AINAHDONFEO_pb2.AINAHDONFEO, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
