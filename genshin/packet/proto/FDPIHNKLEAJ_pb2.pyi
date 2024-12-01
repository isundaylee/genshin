from genshin.packet.proto import NNFDIHPAGHC_pb2 as _NNFDIHPAGHC_pb2
from genshin.packet.proto import MHOJPFGMMHL_pb2 as _MHOJPFGMMHL_pb2
from genshin.packet.proto import DBOLCJJILGP_pb2 as _DBOLCJJILGP_pb2
from genshin.packet.proto import CKBFJJMAKCD_pb2 as _CKBFJJMAKCD_pb2
from genshin.packet.proto import HOFLBHDIPII_pb2 as _HOFLBHDIPII_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FDPIHNKLEAJ(_message.Message):
    __slots__ = ("GCJJEHICMHA", "IHGKAECKDIB", "GJOFKDGPKHN", "KCLFFKGNLBD", "JEGBAICFCIG", "MPFLDFDOGAI")
    class GCJJEHICMHAEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _NNFDIHPAGHC_pb2.NNFDIHPAGHC
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_NNFDIHPAGHC_pb2.NNFDIHPAGHC, _Mapping]] = ...) -> None: ...
    class IHGKAECKDIBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MHOJPFGMMHL_pb2.MHOJPFGMMHL
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MHOJPFGMMHL_pb2.MHOJPFGMMHL, _Mapping]] = ...) -> None: ...
    class GJOFKDGPKHNEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _DBOLCJJILGP_pb2.DBOLCJJILGP
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_DBOLCJJILGP_pb2.DBOLCJJILGP, _Mapping]] = ...) -> None: ...
    GCJJEHICMHA_FIELD_NUMBER: _ClassVar[int]
    IHGKAECKDIB_FIELD_NUMBER: _ClassVar[int]
    GJOFKDGPKHN_FIELD_NUMBER: _ClassVar[int]
    KCLFFKGNLBD_FIELD_NUMBER: _ClassVar[int]
    JEGBAICFCIG_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    GCJJEHICMHA: _containers.MessageMap[int, _NNFDIHPAGHC_pb2.NNFDIHPAGHC]
    IHGKAECKDIB: _containers.MessageMap[int, _MHOJPFGMMHL_pb2.MHOJPFGMMHL]
    GJOFKDGPKHN: _containers.MessageMap[int, _DBOLCJJILGP_pb2.DBOLCJJILGP]
    KCLFFKGNLBD: _CKBFJJMAKCD_pb2.CKBFJJMAKCD
    JEGBAICFCIG: _HOFLBHDIPII_pb2.HOFLBHDIPII
    MPFLDFDOGAI: bool
    def __init__(self, GCJJEHICMHA: _Optional[_Mapping[int, _NNFDIHPAGHC_pb2.NNFDIHPAGHC]] = ..., IHGKAECKDIB: _Optional[_Mapping[int, _MHOJPFGMMHL_pb2.MHOJPFGMMHL]] = ..., GJOFKDGPKHN: _Optional[_Mapping[int, _DBOLCJJILGP_pb2.DBOLCJJILGP]] = ..., KCLFFKGNLBD: _Optional[_Union[_CKBFJJMAKCD_pb2.CKBFJJMAKCD, _Mapping]] = ..., JEGBAICFCIG: _Optional[_Union[_HOFLBHDIPII_pb2.HOFLBHDIPII, _Mapping]] = ..., MPFLDFDOGAI: bool = ...) -> None: ...
