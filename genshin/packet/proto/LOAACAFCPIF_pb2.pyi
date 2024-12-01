from genshin.packet.proto import KNMPNCPBMMP_pb2 as _KNMPNCPBMMP_pb2
from genshin.packet.proto import PCLLABLBNGA_pb2 as _PCLLABLBNGA_pb2
from genshin.packet.proto import OHMLHECHNJO_pb2 as _OHMLHECHNJO_pb2
from genshin.packet.proto import GDHBFFBPIIJ_pb2 as _GDHBFFBPIIJ_pb2
from genshin.packet.proto import IFBALGIDBIO_pb2 as _IFBALGIDBIO_pb2
from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LOAACAFCPIF(_message.Message):
    __slots__ = ("HMLFALPADMC", "HFNFKPKFPNG", "DNDIBGHAPGN", "GGPKAKOCHAI", "GINNLFOLHJJ", "ICOIIKCKKAD")
    HMLFALPADMC_FIELD_NUMBER: _ClassVar[int]
    HFNFKPKFPNG_FIELD_NUMBER: _ClassVar[int]
    DNDIBGHAPGN_FIELD_NUMBER: _ClassVar[int]
    GGPKAKOCHAI_FIELD_NUMBER: _ClassVar[int]
    GINNLFOLHJJ_FIELD_NUMBER: _ClassVar[int]
    ICOIIKCKKAD_FIELD_NUMBER: _ClassVar[int]
    HMLFALPADMC: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    HFNFKPKFPNG: _containers.RepeatedCompositeFieldContainer[_PCLLABLBNGA_pb2.PCLLABLBNGA]
    DNDIBGHAPGN: _OHMLHECHNJO_pb2.OHMLHECHNJO
    GGPKAKOCHAI: _GDHBFFBPIIJ_pb2.GDHBFFBPIIJ
    GINNLFOLHJJ: _IFBALGIDBIO_pb2.IFBALGIDBIO
    ICOIIKCKKAD: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    def __init__(self, HMLFALPADMC: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., HFNFKPKFPNG: _Optional[_Iterable[_Union[_PCLLABLBNGA_pb2.PCLLABLBNGA, _Mapping]]] = ..., DNDIBGHAPGN: _Optional[_Union[_OHMLHECHNJO_pb2.OHMLHECHNJO, _Mapping]] = ..., GGPKAKOCHAI: _Optional[_Union[_GDHBFFBPIIJ_pb2.GDHBFFBPIIJ, _Mapping]] = ..., GINNLFOLHJJ: _Optional[_Union[_IFBALGIDBIO_pb2.IFBALGIDBIO, _Mapping]] = ..., ICOIIKCKKAD: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ...) -> None: ...
