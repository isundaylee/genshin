from genshin.packet.proto import GMPKODPACGM_pb2 as _GMPKODPACGM_pb2
from genshin.packet.proto import GEEMAADBNJI_pb2 as _GEEMAADBNJI_pb2
from genshin.packet.proto import DCBNAHFLEJC_pb2 as _DCBNAHFLEJC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PPDJHNJDEGM(_message.Message):
    __slots__ = ("EANDOCEEMEJ", "PGGECBKBPNP", "EMIPFNGKDPK", "NGLMACPCOEL", "MPFLDFDOGAI", "OPCAGNIDAHI", "NMIKCMLKNDM", "IKAMMKHKKHI")
    class EANDOCEEMEJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _GMPKODPACGM_pb2.GMPKODPACGM
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_GMPKODPACGM_pb2.GMPKODPACGM, _Mapping]] = ...) -> None: ...
    class PGGECBKBPNPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _GEEMAADBNJI_pb2.GEEMAADBNJI
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_GEEMAADBNJI_pb2.GEEMAADBNJI, _Mapping]] = ...) -> None: ...
    EANDOCEEMEJ_FIELD_NUMBER: _ClassVar[int]
    PGGECBKBPNP_FIELD_NUMBER: _ClassVar[int]
    EMIPFNGKDPK_FIELD_NUMBER: _ClassVar[int]
    NGLMACPCOEL_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    OPCAGNIDAHI_FIELD_NUMBER: _ClassVar[int]
    NMIKCMLKNDM_FIELD_NUMBER: _ClassVar[int]
    IKAMMKHKKHI_FIELD_NUMBER: _ClassVar[int]
    EANDOCEEMEJ: _containers.MessageMap[int, _GMPKODPACGM_pb2.GMPKODPACGM]
    PGGECBKBPNP: _containers.MessageMap[int, _GEEMAADBNJI_pb2.GEEMAADBNJI]
    EMIPFNGKDPK: _containers.RepeatedCompositeFieldContainer[_DCBNAHFLEJC_pb2.DCBNAHFLEJC]
    NGLMACPCOEL: int
    MPFLDFDOGAI: bool
    OPCAGNIDAHI: bool
    NMIKCMLKNDM: int
    IKAMMKHKKHI: int
    def __init__(self, EANDOCEEMEJ: _Optional[_Mapping[int, _GMPKODPACGM_pb2.GMPKODPACGM]] = ..., PGGECBKBPNP: _Optional[_Mapping[int, _GEEMAADBNJI_pb2.GEEMAADBNJI]] = ..., EMIPFNGKDPK: _Optional[_Iterable[_Union[_DCBNAHFLEJC_pb2.DCBNAHFLEJC, _Mapping]]] = ..., NGLMACPCOEL: _Optional[int] = ..., MPFLDFDOGAI: bool = ..., OPCAGNIDAHI: bool = ..., NMIKCMLKNDM: _Optional[int] = ..., IKAMMKHKKHI: _Optional[int] = ...) -> None: ...
