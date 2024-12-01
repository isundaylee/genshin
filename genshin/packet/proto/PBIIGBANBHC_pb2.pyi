from genshin.packet.proto import FGNHPFIDPCB_pb2 as _FGNHPFIDPCB_pb2
from genshin.packet.proto import KJIHGCIALOJ_pb2 as _KJIHGCIALOJ_pb2
from genshin.packet.proto import JAFNAFFNFLD_pb2 as _JAFNAFFNFLD_pb2
from genshin.packet.proto import DEIHIELEFEN_pb2 as _DEIHIELEFEN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PBIIGBANBHC(_message.Message):
    __slots__ = ("LEDMFIOGIFL", "HODDLOCGNOB", "MCMJNGOKOJI", "JPNOLKLOAFP", "NGBFPJFAPPE", "MFFPCLGBCDG", "GMJAGIBJEAC", "CHNBJMEFHHB", "PCIAIKNILJF", "BHOJPBGGBNN", "OOJDCIKDBOK", "OHIGHGEANEC", "OHCNLAPPABO")
    LEDMFIOGIFL_FIELD_NUMBER: _ClassVar[int]
    HODDLOCGNOB_FIELD_NUMBER: _ClassVar[int]
    MCMJNGOKOJI_FIELD_NUMBER: _ClassVar[int]
    JPNOLKLOAFP_FIELD_NUMBER: _ClassVar[int]
    NGBFPJFAPPE_FIELD_NUMBER: _ClassVar[int]
    MFFPCLGBCDG_FIELD_NUMBER: _ClassVar[int]
    GMJAGIBJEAC_FIELD_NUMBER: _ClassVar[int]
    CHNBJMEFHHB_FIELD_NUMBER: _ClassVar[int]
    PCIAIKNILJF_FIELD_NUMBER: _ClassVar[int]
    BHOJPBGGBNN_FIELD_NUMBER: _ClassVar[int]
    OOJDCIKDBOK_FIELD_NUMBER: _ClassVar[int]
    OHIGHGEANEC_FIELD_NUMBER: _ClassVar[int]
    OHCNLAPPABO_FIELD_NUMBER: _ClassVar[int]
    LEDMFIOGIFL: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    HODDLOCGNOB: _KJIHGCIALOJ_pb2.KJIHGCIALOJ
    MCMJNGOKOJI: _containers.RepeatedCompositeFieldContainer[_JAFNAFFNFLD_pb2.JAFNAFFNFLD]
    JPNOLKLOAFP: _FGNHPFIDPCB_pb2.FGNHPFIDPCB
    NGBFPJFAPPE: int
    MFFPCLGBCDG: int
    GMJAGIBJEAC: _DEIHIELEFEN_pb2.DEIHIELEFEN
    CHNBJMEFHHB: int
    PCIAIKNILJF: bool
    BHOJPBGGBNN: bool
    OOJDCIKDBOK: bool
    OHIGHGEANEC: int
    OHCNLAPPABO: float
    def __init__(self, LEDMFIOGIFL: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., HODDLOCGNOB: _Optional[_Union[_KJIHGCIALOJ_pb2.KJIHGCIALOJ, _Mapping]] = ..., MCMJNGOKOJI: _Optional[_Iterable[_Union[_JAFNAFFNFLD_pb2.JAFNAFFNFLD, _Mapping]]] = ..., JPNOLKLOAFP: _Optional[_Union[_FGNHPFIDPCB_pb2.FGNHPFIDPCB, _Mapping]] = ..., NGBFPJFAPPE: _Optional[int] = ..., MFFPCLGBCDG: _Optional[int] = ..., GMJAGIBJEAC: _Optional[_Union[_DEIHIELEFEN_pb2.DEIHIELEFEN, str]] = ..., CHNBJMEFHHB: _Optional[int] = ..., PCIAIKNILJF: bool = ..., BHOJPBGGBNN: bool = ..., OOJDCIKDBOK: bool = ..., OHIGHGEANEC: _Optional[int] = ..., OHCNLAPPABO: _Optional[float] = ...) -> None: ...
