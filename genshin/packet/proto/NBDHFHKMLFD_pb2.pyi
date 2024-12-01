from genshin.packet.proto import EPPEGDIEFJN_pb2 as _EPPEGDIEFJN_pb2
from genshin.packet.proto import PKJMPCPEGGO_pb2 as _PKJMPCPEGGO_pb2
from genshin.packet.proto import HKAMLCIMKJL_pb2 as _HKAMLCIMKJL_pb2
from genshin.packet.proto import NFONHFAMDNE_pb2 as _NFONHFAMDNE_pb2
from genshin.packet.proto import GLNNDHIHPDF_pb2 as _GLNNDHIHPDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NBDHFHKMLFD(_message.Message):
    __slots__ = ("OMKNBNMEBIK", "BMFKOONMMEE", "DKHHPAJBJIF", "LBKDGOEFEBC", "IJLHLCLLENE", "EFAJIHMNOBK", "HILLLCLAILE", "IANEBDKAMBM", "HLOLOOCLKAP", "NDIKNHFCCIC", "FCPANCMAOIE", "KIIHMCAHNPM", "level", "AJCGKKPCCGD", "MKHENDMFLMF", "avatar_id", "HDBFKNJHBOO", "FIDHNDFHEDA", "PCACHAGGINN", "FAKDLEIHGML", "DPLLLEKLOEI", "NEANBGINFPF", "NCCPPHNNPBF", "MBENIIJDLNA", "BBHEIPKNPHC", "JADDAKOJMBB", "AMIKDFCMBMP")
    OMKNBNMEBIK_FIELD_NUMBER: _ClassVar[int]
    BMFKOONMMEE_FIELD_NUMBER: _ClassVar[int]
    DKHHPAJBJIF_FIELD_NUMBER: _ClassVar[int]
    LBKDGOEFEBC_FIELD_NUMBER: _ClassVar[int]
    IJLHLCLLENE_FIELD_NUMBER: _ClassVar[int]
    EFAJIHMNOBK_FIELD_NUMBER: _ClassVar[int]
    HILLLCLAILE_FIELD_NUMBER: _ClassVar[int]
    IANEBDKAMBM_FIELD_NUMBER: _ClassVar[int]
    HLOLOOCLKAP_FIELD_NUMBER: _ClassVar[int]
    NDIKNHFCCIC_FIELD_NUMBER: _ClassVar[int]
    FCPANCMAOIE_FIELD_NUMBER: _ClassVar[int]
    KIIHMCAHNPM_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    AJCGKKPCCGD_FIELD_NUMBER: _ClassVar[int]
    MKHENDMFLMF_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    HDBFKNJHBOO_FIELD_NUMBER: _ClassVar[int]
    FIDHNDFHEDA_FIELD_NUMBER: _ClassVar[int]
    PCACHAGGINN_FIELD_NUMBER: _ClassVar[int]
    FAKDLEIHGML_FIELD_NUMBER: _ClassVar[int]
    DPLLLEKLOEI_FIELD_NUMBER: _ClassVar[int]
    NEANBGINFPF_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    MBENIIJDLNA_FIELD_NUMBER: _ClassVar[int]
    BBHEIPKNPHC_FIELD_NUMBER: _ClassVar[int]
    JADDAKOJMBB_FIELD_NUMBER: _ClassVar[int]
    AMIKDFCMBMP_FIELD_NUMBER: _ClassVar[int]
    OMKNBNMEBIK: str
    BMFKOONMMEE: str
    DKHHPAJBJIF: str
    LBKDGOEFEBC: str
    IJLHLCLLENE: str
    EFAJIHMNOBK: str
    HILLLCLAILE: _containers.RepeatedCompositeFieldContainer[_EPPEGDIEFJN_pb2.EPPEGDIEFJN]
    IANEBDKAMBM: _PKJMPCPEGGO_pb2.PKJMPCPEGGO
    HLOLOOCLKAP: int
    NDIKNHFCCIC: int
    FCPANCMAOIE: int
    KIIHMCAHNPM: _HKAMLCIMKJL_pb2.HKAMLCIMKJL
    level: int
    AJCGKKPCCGD: _NFONHFAMDNE_pb2.NFONHFAMDNE
    MKHENDMFLMF: int
    avatar_id: int
    HDBFKNJHBOO: int
    FIDHNDFHEDA: int
    PCACHAGGINN: bool
    FAKDLEIHGML: bool
    DPLLLEKLOEI: bool
    NEANBGINFPF: bool
    NCCPPHNNPBF: int
    MBENIIJDLNA: _GLNNDHIHPDF_pb2.GLNNDHIHPDF
    BBHEIPKNPHC: bool
    JADDAKOJMBB: bool
    AMIKDFCMBMP: bool
    def __init__(self, OMKNBNMEBIK: _Optional[str] = ..., BMFKOONMMEE: _Optional[str] = ..., DKHHPAJBJIF: _Optional[str] = ..., LBKDGOEFEBC: _Optional[str] = ..., IJLHLCLLENE: _Optional[str] = ..., EFAJIHMNOBK: _Optional[str] = ..., HILLLCLAILE: _Optional[_Iterable[_Union[_EPPEGDIEFJN_pb2.EPPEGDIEFJN, _Mapping]]] = ..., IANEBDKAMBM: _Optional[_Union[_PKJMPCPEGGO_pb2.PKJMPCPEGGO, _Mapping]] = ..., HLOLOOCLKAP: _Optional[int] = ..., NDIKNHFCCIC: _Optional[int] = ..., FCPANCMAOIE: _Optional[int] = ..., KIIHMCAHNPM: _Optional[_Union[_HKAMLCIMKJL_pb2.HKAMLCIMKJL, str]] = ..., level: _Optional[int] = ..., AJCGKKPCCGD: _Optional[_Union[_NFONHFAMDNE_pb2.NFONHFAMDNE, str]] = ..., MKHENDMFLMF: _Optional[int] = ..., avatar_id: _Optional[int] = ..., HDBFKNJHBOO: _Optional[int] = ..., FIDHNDFHEDA: _Optional[int] = ..., PCACHAGGINN: bool = ..., FAKDLEIHGML: bool = ..., DPLLLEKLOEI: bool = ..., NEANBGINFPF: bool = ..., NCCPPHNNPBF: _Optional[int] = ..., MBENIIJDLNA: _Optional[_Union[_GLNNDHIHPDF_pb2.GLNNDHIHPDF, str]] = ..., BBHEIPKNPHC: bool = ..., JADDAKOJMBB: bool = ..., AMIKDFCMBMP: bool = ...) -> None: ...
