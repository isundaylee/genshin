from genshin.packet.proto import FMJEDPAOJDN_pb2 as _FMJEDPAOJDN_pb2
from genshin.packet.proto import MMGMJPJHJLL_pb2 as _MMGMJPJHJLL_pb2
from genshin.packet.proto import NGDFAGGMLHB_pb2 as _NGDFAGGMLHB_pb2
from genshin.packet.proto import EBHCMMIHDJL_pb2 as _EBHCMMIHDJL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ONCDPLGELHG(_message.Message):
    __slots__ = ("KCBLAFECKCH", "BCIFJFNNJJM", "JADIDDIBHPF", "CGGMEDEICFL", "BBHHOLEOHNO", "level", "HGBBGLKPLFI", "exp", "HEPIBKMFGJI", "JCCKKCMGFME")
    KCBLAFECKCH_FIELD_NUMBER: _ClassVar[int]
    BCIFJFNNJJM_FIELD_NUMBER: _ClassVar[int]
    JADIDDIBHPF_FIELD_NUMBER: _ClassVar[int]
    CGGMEDEICFL_FIELD_NUMBER: _ClassVar[int]
    BBHHOLEOHNO_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    HGBBGLKPLFI_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    HEPIBKMFGJI_FIELD_NUMBER: _ClassVar[int]
    JCCKKCMGFME_FIELD_NUMBER: _ClassVar[int]
    KCBLAFECKCH: _FMJEDPAOJDN_pb2.FMJEDPAOJDN
    BCIFJFNNJJM: _MMGMJPJHJLL_pb2.MMGMJPJHJLL
    JADIDDIBHPF: _NGDFAGGMLHB_pb2.NGDFAGGMLHB
    CGGMEDEICFL: _containers.RepeatedScalarFieldContainer[int]
    BBHHOLEOHNO: _EBHCMMIHDJL_pb2.EBHCMMIHDJL
    level: int
    HGBBGLKPLFI: int
    exp: int
    HEPIBKMFGJI: int
    JCCKKCMGFME: int
    def __init__(self, KCBLAFECKCH: _Optional[_Union[_FMJEDPAOJDN_pb2.FMJEDPAOJDN, _Mapping]] = ..., BCIFJFNNJJM: _Optional[_Union[_MMGMJPJHJLL_pb2.MMGMJPJHJLL, _Mapping]] = ..., JADIDDIBHPF: _Optional[_Union[_NGDFAGGMLHB_pb2.NGDFAGGMLHB, _Mapping]] = ..., CGGMEDEICFL: _Optional[_Iterable[int]] = ..., BBHHOLEOHNO: _Optional[_Union[_EBHCMMIHDJL_pb2.EBHCMMIHDJL, _Mapping]] = ..., level: _Optional[int] = ..., HGBBGLKPLFI: _Optional[int] = ..., exp: _Optional[int] = ..., HEPIBKMFGJI: _Optional[int] = ..., JCCKKCMGFME: _Optional[int] = ...) -> None: ...
