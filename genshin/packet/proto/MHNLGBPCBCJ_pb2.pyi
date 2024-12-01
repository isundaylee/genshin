from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import ECKACOBPKBL_pb2 as _ECKACOBPKBL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MHNLGBPCBCJ(_message.Message):
    __slots__ = ("CKBILFDELIF", "AMFBNEJGHMA", "NOHGCKAMBJC", "IGBDOEBPPHO", "NJDDAOLLMGI")
    CKBILFDELIF_FIELD_NUMBER: _ClassVar[int]
    AMFBNEJGHMA_FIELD_NUMBER: _ClassVar[int]
    NOHGCKAMBJC_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    NJDDAOLLMGI_FIELD_NUMBER: _ClassVar[int]
    CKBILFDELIF: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    AMFBNEJGHMA: _containers.RepeatedCompositeFieldContainer[_ECKACOBPKBL_pb2.ECKACOBPKBL]
    NOHGCKAMBJC: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    IGBDOEBPPHO: int
    NJDDAOLLMGI: int
    def __init__(self, CKBILFDELIF: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., AMFBNEJGHMA: _Optional[_Iterable[_Union[_ECKACOBPKBL_pb2.ECKACOBPKBL, _Mapping]]] = ..., NOHGCKAMBJC: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., IGBDOEBPPHO: _Optional[int] = ..., NJDDAOLLMGI: _Optional[int] = ...) -> None: ...
