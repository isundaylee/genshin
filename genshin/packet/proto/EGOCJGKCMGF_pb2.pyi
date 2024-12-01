from genshin.packet.proto import PDEPCEHJHJJ_pb2 as _PDEPCEHJHJJ_pb2
from genshin.packet.proto import FIHNKIBGLHA_pb2 as _FIHNKIBGLHA_pb2
from genshin.packet.proto import PENDPGJGCKD_pb2 as _PENDPGJGCKD_pb2
from genshin.packet.proto import KCCFEHJJDGL_pb2 as _KCCFEHJJDGL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EGOCJGKCMGF(_message.Message):
    __slots__ = ("CGGMEDEICFL", "NPLOCJAEIBE", "KCBLAFECKCH", "BCIFJFNNJJM", "JADIDDIBHPF", "FAGPPHACNBJ", "HGBBGLKPLFI", "HEPIBKMFGJI", "level", "exp", "FMHPJLFHLFM")
    CGGMEDEICFL_FIELD_NUMBER: _ClassVar[int]
    NPLOCJAEIBE_FIELD_NUMBER: _ClassVar[int]
    KCBLAFECKCH_FIELD_NUMBER: _ClassVar[int]
    BCIFJFNNJJM_FIELD_NUMBER: _ClassVar[int]
    JADIDDIBHPF_FIELD_NUMBER: _ClassVar[int]
    FAGPPHACNBJ_FIELD_NUMBER: _ClassVar[int]
    HGBBGLKPLFI_FIELD_NUMBER: _ClassVar[int]
    HEPIBKMFGJI_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    FMHPJLFHLFM_FIELD_NUMBER: _ClassVar[int]
    CGGMEDEICFL: _containers.RepeatedScalarFieldContainer[int]
    NPLOCJAEIBE: _PDEPCEHJHJJ_pb2.PDEPCEHJHJJ
    KCBLAFECKCH: _FIHNKIBGLHA_pb2.FIHNKIBGLHA
    BCIFJFNNJJM: _PENDPGJGCKD_pb2.PENDPGJGCKD
    JADIDDIBHPF: _KCCFEHJJDGL_pb2.KCCFEHJJDGL
    FAGPPHACNBJ: int
    HGBBGLKPLFI: int
    HEPIBKMFGJI: int
    level: int
    exp: int
    FMHPJLFHLFM: int
    def __init__(self, CGGMEDEICFL: _Optional[_Iterable[int]] = ..., NPLOCJAEIBE: _Optional[_Union[_PDEPCEHJHJJ_pb2.PDEPCEHJHJJ, _Mapping]] = ..., KCBLAFECKCH: _Optional[_Union[_FIHNKIBGLHA_pb2.FIHNKIBGLHA, _Mapping]] = ..., BCIFJFNNJJM: _Optional[_Union[_PENDPGJGCKD_pb2.PENDPGJGCKD, _Mapping]] = ..., JADIDDIBHPF: _Optional[_Union[_KCCFEHJJDGL_pb2.KCCFEHJJDGL, _Mapping]] = ..., FAGPPHACNBJ: _Optional[int] = ..., HGBBGLKPLFI: _Optional[int] = ..., HEPIBKMFGJI: _Optional[int] = ..., level: _Optional[int] = ..., exp: _Optional[int] = ..., FMHPJLFHLFM: _Optional[int] = ...) -> None: ...
