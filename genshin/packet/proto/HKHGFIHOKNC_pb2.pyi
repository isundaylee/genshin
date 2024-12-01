from genshin.packet.proto import DFOKMEDFPLL_pb2 as _DFOKMEDFPLL_pb2
from genshin.packet.proto import BPGCAHBJNCD_pb2 as _BPGCAHBJNCD_pb2
from genshin.packet.proto import EHCLPIIPLOH_pb2 as _EHCLPIIPLOH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HKHGFIHOKNC(_message.Message):
    __slots__ = ("MKOFAGFGOIA", "INFHJIEPNJD", "item_list", "MHJHGIMLHLN", "HLKDDNGCKJN", "PICOLPBCPGH", "BKAMPGBBBFP", "BHEBPJKAGMO", "NBDGKGPLBOE", "DBPCFFBOECF", "DEDDKKOGEIL")
    MKOFAGFGOIA_FIELD_NUMBER: _ClassVar[int]
    INFHJIEPNJD_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    MHJHGIMLHLN_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    PICOLPBCPGH_FIELD_NUMBER: _ClassVar[int]
    BKAMPGBBBFP_FIELD_NUMBER: _ClassVar[int]
    BHEBPJKAGMO_FIELD_NUMBER: _ClassVar[int]
    NBDGKGPLBOE_FIELD_NUMBER: _ClassVar[int]
    DBPCFFBOECF_FIELD_NUMBER: _ClassVar[int]
    DEDDKKOGEIL_FIELD_NUMBER: _ClassVar[int]
    MKOFAGFGOIA: _containers.RepeatedScalarFieldContainer[str]
    INFHJIEPNJD: _DFOKMEDFPLL_pb2.DFOKMEDFPLL
    item_list: _containers.RepeatedCompositeFieldContainer[_BPGCAHBJNCD_pb2.BPGCAHBJNCD]
    MHJHGIMLHLN: int
    HLKDDNGCKJN: int
    PICOLPBCPGH: bool
    BKAMPGBBBFP: bool
    BHEBPJKAGMO: int
    NBDGKGPLBOE: int
    DBPCFFBOECF: _EHCLPIIPLOH_pb2.EHCLPIIPLOH
    DEDDKKOGEIL: int
    def __init__(self, MKOFAGFGOIA: _Optional[_Iterable[str]] = ..., INFHJIEPNJD: _Optional[_Union[_DFOKMEDFPLL_pb2.DFOKMEDFPLL, _Mapping]] = ..., item_list: _Optional[_Iterable[_Union[_BPGCAHBJNCD_pb2.BPGCAHBJNCD, _Mapping]]] = ..., MHJHGIMLHLN: _Optional[int] = ..., HLKDDNGCKJN: _Optional[int] = ..., PICOLPBCPGH: bool = ..., BKAMPGBBBFP: bool = ..., BHEBPJKAGMO: _Optional[int] = ..., NBDGKGPLBOE: _Optional[int] = ..., DBPCFFBOECF: _Optional[_Union[_EHCLPIIPLOH_pb2.EHCLPIIPLOH, str]] = ..., DEDDKKOGEIL: _Optional[int] = ...) -> None: ...
