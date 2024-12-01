from genshin.packet.proto import NDOEDPNDPBH_pb2 as _NDOEDPNDPBH_pb2
from genshin.packet.proto import OADJBKDJNPL_pb2 as _OADJBKDJNPL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GPPNDKHNOBM(_message.Message):
    __slots__ = ("LJIDOHLADHC", "EOMNMODEDFD", "MJPEDPOIFLM", "BJNIKAKPONA", "AKJPODMJNEH")
    LJIDOHLADHC_FIELD_NUMBER: _ClassVar[int]
    EOMNMODEDFD_FIELD_NUMBER: _ClassVar[int]
    MJPEDPOIFLM_FIELD_NUMBER: _ClassVar[int]
    BJNIKAKPONA_FIELD_NUMBER: _ClassVar[int]
    AKJPODMJNEH_FIELD_NUMBER: _ClassVar[int]
    LJIDOHLADHC: _NDOEDPNDPBH_pb2.NDOEDPNDPBH
    EOMNMODEDFD: _OADJBKDJNPL_pb2.OADJBKDJNPL
    MJPEDPOIFLM: bool
    BJNIKAKPONA: bool
    AKJPODMJNEH: int
    def __init__(self, LJIDOHLADHC: _Optional[_Union[_NDOEDPNDPBH_pb2.NDOEDPNDPBH, _Mapping]] = ..., EOMNMODEDFD: _Optional[_Union[_OADJBKDJNPL_pb2.OADJBKDJNPL, _Mapping]] = ..., MJPEDPOIFLM: bool = ..., BJNIKAKPONA: bool = ..., AKJPODMJNEH: _Optional[int] = ...) -> None: ...
