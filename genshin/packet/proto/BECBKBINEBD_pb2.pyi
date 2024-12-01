from genshin.packet.proto import IKDFPLIKJCP_pb2 as _IKDFPLIKJCP_pb2
from genshin.packet.proto import BLCAPEBDFDM_pb2 as _BLCAPEBDFDM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BECBKBINEBD(_message.Message):
    __slots__ = ("GIKJPJGMPAM", "BENPELLBBJC", "OOIPGFEDJMN", "DFOPEDHMDFK")
    GIKJPJGMPAM_FIELD_NUMBER: _ClassVar[int]
    BENPELLBBJC_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    DFOPEDHMDFK_FIELD_NUMBER: _ClassVar[int]
    GIKJPJGMPAM: _containers.RepeatedCompositeFieldContainer[_IKDFPLIKJCP_pb2.IKDFPLIKJCP]
    BENPELLBBJC: int
    OOIPGFEDJMN: int
    DFOPEDHMDFK: _BLCAPEBDFDM_pb2.BLCAPEBDFDM
    def __init__(self, GIKJPJGMPAM: _Optional[_Iterable[_Union[_IKDFPLIKJCP_pb2.IKDFPLIKJCP, _Mapping]]] = ..., BENPELLBBJC: _Optional[int] = ..., OOIPGFEDJMN: _Optional[int] = ..., DFOPEDHMDFK: _Optional[_Union[_BLCAPEBDFDM_pb2.BLCAPEBDFDM, str]] = ...) -> None: ...
