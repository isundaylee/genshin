from genshin.packet.proto import AHDCNHCIBNM_pb2 as _AHDCNHCIBNM_pb2
from genshin.packet.proto import CKKGDKCKLKH_pb2 as _CKKGDKCKLKH_pb2
from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import BAECKBPLJAG_pb2 as _BAECKBPLJAG_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NILMHFAANPL(_message.Message):
    __slots__ = ("EJNOCLDGPEF", "BJCABOBCJCE", "HPOECKEKAFA", "MCJNLBADFIN", "DGOCEFOFCNK", "LLADMBNFOAM")
    EJNOCLDGPEF_FIELD_NUMBER: _ClassVar[int]
    BJCABOBCJCE_FIELD_NUMBER: _ClassVar[int]
    HPOECKEKAFA_FIELD_NUMBER: _ClassVar[int]
    MCJNLBADFIN_FIELD_NUMBER: _ClassVar[int]
    DGOCEFOFCNK_FIELD_NUMBER: _ClassVar[int]
    LLADMBNFOAM_FIELD_NUMBER: _ClassVar[int]
    EJNOCLDGPEF: _AHDCNHCIBNM_pb2.AHDCNHCIBNM
    BJCABOBCJCE: _CKKGDKCKLKH_pb2.CKKGDKCKLKH
    HPOECKEKAFA: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    MCJNLBADFIN: _BAECKBPLJAG_pb2.BAECKBPLJAG
    DGOCEFOFCNK: int
    LLADMBNFOAM: int
    def __init__(self, EJNOCLDGPEF: _Optional[_Union[_AHDCNHCIBNM_pb2.AHDCNHCIBNM, _Mapping]] = ..., BJCABOBCJCE: _Optional[_Union[_CKKGDKCKLKH_pb2.CKKGDKCKLKH, _Mapping]] = ..., HPOECKEKAFA: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., MCJNLBADFIN: _Optional[_Union[_BAECKBPLJAG_pb2.BAECKBPLJAG, str]] = ..., DGOCEFOFCNK: _Optional[int] = ..., LLADMBNFOAM: _Optional[int] = ...) -> None: ...
