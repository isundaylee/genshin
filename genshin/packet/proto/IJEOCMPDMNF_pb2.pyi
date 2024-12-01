from genshin.packet.proto import GKIDJMLNNHH_pb2 as _GKIDJMLNNHH_pb2
from genshin.packet.proto import NIPGCFOGIHP_pb2 as _NIPGCFOGIHP_pb2
from genshin.packet.proto import NIHODIJKPKE_pb2 as _NIHODIJKPKE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IJEOCMPDMNF(_message.Message):
    __slots__ = ("MIHAKFPLLKC", "CBNGGOBIDHA", "PNDPNMBDOKF", "FBLPAKODJCJ", "MPFLDFDOGAI", "HDIHDAJMLFF")
    MIHAKFPLLKC_FIELD_NUMBER: _ClassVar[int]
    CBNGGOBIDHA_FIELD_NUMBER: _ClassVar[int]
    PNDPNMBDOKF_FIELD_NUMBER: _ClassVar[int]
    FBLPAKODJCJ_FIELD_NUMBER: _ClassVar[int]
    MPFLDFDOGAI_FIELD_NUMBER: _ClassVar[int]
    HDIHDAJMLFF_FIELD_NUMBER: _ClassVar[int]
    MIHAKFPLLKC: _GKIDJMLNNHH_pb2.GKIDJMLNNHH
    CBNGGOBIDHA: _NIPGCFOGIHP_pb2.NIPGCFOGIHP
    PNDPNMBDOKF: _containers.RepeatedCompositeFieldContainer[_NIHODIJKPKE_pb2.NIHODIJKPKE]
    FBLPAKODJCJ: bool
    MPFLDFDOGAI: bool
    HDIHDAJMLFF: bool
    def __init__(self, MIHAKFPLLKC: _Optional[_Union[_GKIDJMLNNHH_pb2.GKIDJMLNNHH, _Mapping]] = ..., CBNGGOBIDHA: _Optional[_Union[_NIPGCFOGIHP_pb2.NIPGCFOGIHP, _Mapping]] = ..., PNDPNMBDOKF: _Optional[_Iterable[_Union[_NIHODIJKPKE_pb2.NIHODIJKPKE, _Mapping]]] = ..., FBLPAKODJCJ: bool = ..., MPFLDFDOGAI: bool = ..., HDIHDAJMLFF: bool = ...) -> None: ...
