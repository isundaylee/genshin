from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import OMDEFNFDGCF_pb2 as _OMDEFNFDGCF_pb2
from genshin.packet.proto import HMFFLJOGOIA_pb2 as _HMFFLJOGOIA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CAHHBEHNCGL(_message.Message):
    __slots__ = ("GJEBAJAJPII", "MCJNLBADFIN", "sphere_radius", "cylinder_size", "cubic_size", "polygon_size", "EHAEACFBOOL", "HLKDDNGCKJN")
    GJEBAJAJPII_FIELD_NUMBER: _ClassVar[int]
    MCJNLBADFIN_FIELD_NUMBER: _ClassVar[int]
    SPHERE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    CUBIC_SIZE_FIELD_NUMBER: _ClassVar[int]
    POLYGON_SIZE_FIELD_NUMBER: _ClassVar[int]
    EHAEACFBOOL_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    GJEBAJAJPII: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    MCJNLBADFIN: int
    sphere_radius: float
    cylinder_size: _OMDEFNFDGCF_pb2.OMDEFNFDGCF
    cubic_size: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    polygon_size: _HMFFLJOGOIA_pb2.HMFFLJOGOIA
    EHAEACFBOOL: int
    HLKDDNGCKJN: int
    def __init__(self, GJEBAJAJPII: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., MCJNLBADFIN: _Optional[int] = ..., sphere_radius: _Optional[float] = ..., cylinder_size: _Optional[_Union[_OMDEFNFDGCF_pb2.OMDEFNFDGCF, _Mapping]] = ..., cubic_size: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., polygon_size: _Optional[_Union[_HMFFLJOGOIA_pb2.HMFFLJOGOIA, _Mapping]] = ..., EHAEACFBOOL: _Optional[int] = ..., HLKDDNGCKJN: _Optional[int] = ...) -> None: ...
