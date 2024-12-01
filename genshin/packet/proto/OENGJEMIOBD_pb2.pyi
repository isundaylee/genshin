from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import GIJCLDFPLMH_pb2 as _GIJCLDFPLMH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OENGJEMIOBD(_message.Message):
    __slots__ = ("DOALEGICGKL", "GJEBAJAJPII", "NCCPPHNNPBF", "IMIOGMDOKCB")
    DOALEGICGKL_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    DOALEGICGKL: _containers.RepeatedScalarFieldContainer[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    NCCPPHNNPBF: int
    IMIOGMDOKCB: _GIJCLDFPLMH_pb2.GIJCLDFPLMH
    def __init__(self, DOALEGICGKL: _Optional[_Iterable[int]] = ..., GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., NCCPPHNNPBF: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_GIJCLDFPLMH_pb2.GIJCLDFPLMH, str]] = ...) -> None: ...
