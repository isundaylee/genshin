from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import MAODFHOMKOB_pb2 as _MAODFHOMKOB_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LKPMOBAIJIG(_message.Message):
    __slots__ = ("FGFLJIAEMLJ", "GJEBAJAJPII", "IGBDOEBPPHO", "IMIOGMDOKCB")
    FGFLJIAEMLJ_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    FGFLJIAEMLJ: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    IGBDOEBPPHO: int
    IMIOGMDOKCB: _MAODFHOMKOB_pb2.MAODFHOMKOB
    def __init__(self, FGFLJIAEMLJ: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., IGBDOEBPPHO: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_MAODFHOMKOB_pb2.MAODFHOMKOB, str]] = ...) -> None: ...
