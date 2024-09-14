from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MusicGameSettleReq(_message.Message):
    __slots__ = ("correct_hit", "OEAHADEGEOA", "ugc_guid", "BPNLLFDJJOL", "score", "MECALGKAKJK", "max_combo", "KPPICEDHMPN", "speed", "KDAOEDCLEFG", "is_save_score", "MAMHOPGFOKD", "NMPPJPOJFDC", "music_basic_id", "combo", "NGALDEAEBHG", "FCFNKIDLDHJ", "GDOMKIHOKCC")
    CORRECT_HIT_FIELD_NUMBER: _ClassVar[int]
    OEAHADEGEOA_FIELD_NUMBER: _ClassVar[int]
    UGC_GUID_FIELD_NUMBER: _ClassVar[int]
    BPNLLFDJJOL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MECALGKAKJK_FIELD_NUMBER: _ClassVar[int]
    MAX_COMBO_FIELD_NUMBER: _ClassVar[int]
    KPPICEDHMPN_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    KDAOEDCLEFG_FIELD_NUMBER: _ClassVar[int]
    IS_SAVE_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAMHOPGFOKD_FIELD_NUMBER: _ClassVar[int]
    NMPPJPOJFDC_FIELD_NUMBER: _ClassVar[int]
    MUSIC_BASIC_ID_FIELD_NUMBER: _ClassVar[int]
    COMBO_FIELD_NUMBER: _ClassVar[int]
    NGALDEAEBHG_FIELD_NUMBER: _ClassVar[int]
    FCFNKIDLDHJ_FIELD_NUMBER: _ClassVar[int]
    GDOMKIHOKCC_FIELD_NUMBER: _ClassVar[int]
    correct_hit: int
    OEAHADEGEOA: _containers.RepeatedScalarFieldContainer[int]
    ugc_guid: int
    BPNLLFDJJOL: bool
    score: int
    MECALGKAKJK: int
    max_combo: int
    KPPICEDHMPN: _containers.RepeatedScalarFieldContainer[int]
    speed: float
    KDAOEDCLEFG: int
    is_save_score: bool
    MAMHOPGFOKD: bool
    NMPPJPOJFDC: int
    music_basic_id: int
    combo: int
    NGALDEAEBHG: int
    FCFNKIDLDHJ: int
    GDOMKIHOKCC: int
    def __init__(self, correct_hit: _Optional[int] = ..., OEAHADEGEOA: _Optional[_Iterable[int]] = ..., ugc_guid: _Optional[int] = ..., BPNLLFDJJOL: bool = ..., score: _Optional[int] = ..., MECALGKAKJK: _Optional[int] = ..., max_combo: _Optional[int] = ..., KPPICEDHMPN: _Optional[_Iterable[int]] = ..., speed: _Optional[float] = ..., KDAOEDCLEFG: _Optional[int] = ..., is_save_score: bool = ..., MAMHOPGFOKD: bool = ..., NMPPJPOJFDC: _Optional[int] = ..., music_basic_id: _Optional[int] = ..., combo: _Optional[int] = ..., NGALDEAEBHG: _Optional[int] = ..., FCFNKIDLDHJ: _Optional[int] = ..., GDOMKIHOKCC: _Optional[int] = ...) -> None: ...
