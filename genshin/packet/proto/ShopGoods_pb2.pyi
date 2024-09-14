from genshin.packet.proto import ItemParam_pb2 as _ItemParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShopGoods(_message.Message):
    __slots__ = ("NJCCEMPMHDI", "begin_time", "next_refresh_time", "CJMMGKPFMOF", "DJJOHOKKDBM", "goods_item", "HDHJDCPHFMK", "LPAHJGDBEPE", "IBCGFFJGCID", "HKBHNINJMLN", "goods_id", "KMBAMPPHCNI", "GIICBPIGICM", "bought_num", "end_time", "JLIBGEFCAHD", "BHNAJCLPOJE", "KJAGOOHCNON", "AFOGAPGJCOH", "EHIAIOONFDH", "MNCAAIMGCJJ")
    NJCCEMPMHDI_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    CJMMGKPFMOF_FIELD_NUMBER: _ClassVar[int]
    DJJOHOKKDBM_FIELD_NUMBER: _ClassVar[int]
    GOODS_ITEM_FIELD_NUMBER: _ClassVar[int]
    HDHJDCPHFMK_FIELD_NUMBER: _ClassVar[int]
    LPAHJGDBEPE_FIELD_NUMBER: _ClassVar[int]
    IBCGFFJGCID_FIELD_NUMBER: _ClassVar[int]
    HKBHNINJMLN_FIELD_NUMBER: _ClassVar[int]
    GOODS_ID_FIELD_NUMBER: _ClassVar[int]
    KMBAMPPHCNI_FIELD_NUMBER: _ClassVar[int]
    GIICBPIGICM_FIELD_NUMBER: _ClassVar[int]
    BOUGHT_NUM_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    JLIBGEFCAHD_FIELD_NUMBER: _ClassVar[int]
    BHNAJCLPOJE_FIELD_NUMBER: _ClassVar[int]
    KJAGOOHCNON_FIELD_NUMBER: _ClassVar[int]
    AFOGAPGJCOH_FIELD_NUMBER: _ClassVar[int]
    EHIAIOONFDH_FIELD_NUMBER: _ClassVar[int]
    MNCAAIMGCJJ_FIELD_NUMBER: _ClassVar[int]
    NJCCEMPMHDI: int
    begin_time: int
    next_refresh_time: int
    CJMMGKPFMOF: int
    DJJOHOKKDBM: int
    goods_item: _ItemParam_pb2.ItemParam
    HDHJDCPHFMK: int
    LPAHJGDBEPE: int
    IBCGFFJGCID: int
    HKBHNINJMLN: int
    goods_id: int
    KMBAMPPHCNI: _containers.RepeatedCompositeFieldContainer[_ItemParam_pb2.ItemParam]
    GIICBPIGICM: _containers.RepeatedScalarFieldContainer[int]
    bought_num: int
    end_time: int
    JLIBGEFCAHD: int
    BHNAJCLPOJE: int
    KJAGOOHCNON: int
    AFOGAPGJCOH: int
    EHIAIOONFDH: bool
    MNCAAIMGCJJ: int
    def __init__(self, NJCCEMPMHDI: _Optional[int] = ..., begin_time: _Optional[int] = ..., next_refresh_time: _Optional[int] = ..., CJMMGKPFMOF: _Optional[int] = ..., DJJOHOKKDBM: _Optional[int] = ..., goods_item: _Optional[_Union[_ItemParam_pb2.ItemParam, _Mapping]] = ..., HDHJDCPHFMK: _Optional[int] = ..., LPAHJGDBEPE: _Optional[int] = ..., IBCGFFJGCID: _Optional[int] = ..., HKBHNINJMLN: _Optional[int] = ..., goods_id: _Optional[int] = ..., KMBAMPPHCNI: _Optional[_Iterable[_Union[_ItemParam_pb2.ItemParam, _Mapping]]] = ..., GIICBPIGICM: _Optional[_Iterable[int]] = ..., bought_num: _Optional[int] = ..., end_time: _Optional[int] = ..., JLIBGEFCAHD: _Optional[int] = ..., BHNAJCLPOJE: _Optional[int] = ..., KJAGOOHCNON: _Optional[int] = ..., AFOGAPGJCOH: _Optional[int] = ..., EHIAIOONFDH: bool = ..., MNCAAIMGCJJ: _Optional[int] = ...) -> None: ...
