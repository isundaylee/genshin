from genshin.packet.proto import CKKGDKCKLKH_pb2 as _CKKGDKCKLKH_pb2
from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import AHDCNHCIBNM_pb2 as _AHDCNHCIBNM_pb2
from genshin.packet.proto import BAECKBPLJAG_pb2 as _BAECKBPLJAG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFFIOKDNCLP(_message.Message):
    __slots__ = ("BJCABOBCJCE", "HPOECKEKAFA", "EJNOCLDGPEF", "DGOCEFOFCNK", "MCJNLBADFIN")
    BJCABOBCJCE_FIELD_NUMBER: _ClassVar[int]
    HPOECKEKAFA_FIELD_NUMBER: _ClassVar[int]
    EJNOCLDGPEF_FIELD_NUMBER: _ClassVar[int]
    DGOCEFOFCNK_FIELD_NUMBER: _ClassVar[int]
    MCJNLBADFIN_FIELD_NUMBER: _ClassVar[int]
    BJCABOBCJCE: _CKKGDKCKLKH_pb2.CKKGDKCKLKH
    HPOECKEKAFA: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    EJNOCLDGPEF: _AHDCNHCIBNM_pb2.AHDCNHCIBNM
    DGOCEFOFCNK: int
    MCJNLBADFIN: _BAECKBPLJAG_pb2.BAECKBPLJAG
    def __init__(self, BJCABOBCJCE: _Optional[_Union[_CKKGDKCKLKH_pb2.CKKGDKCKLKH, _Mapping]] = ..., HPOECKEKAFA: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., EJNOCLDGPEF: _Optional[_Union[_AHDCNHCIBNM_pb2.AHDCNHCIBNM, _Mapping]] = ..., DGOCEFOFCNK: _Optional[int] = ..., MCJNLBADFIN: _Optional[_Union[_BAECKBPLJAG_pb2.BAECKBPLJAG, str]] = ...) -> None: ...
