from genshin.packet.proto import JIHHHAPKBEH_pb2 as _JIHHHAPKBEH_pb2
from genshin.packet.proto import MGGAHFOAMJF_pb2 as _MGGAHFOAMJF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KIBLANEDMOA(_message.Message):
    __slots__ = ("FEHOKHCMJPD", "LFODPPNBHMN", "NCCPPHNNPBF", "OPHGAPAHHKC")
    FEHOKHCMJPD_FIELD_NUMBER: _ClassVar[int]
    LFODPPNBHMN_FIELD_NUMBER: _ClassVar[int]
    NCCPPHNNPBF_FIELD_NUMBER: _ClassVar[int]
    OPHGAPAHHKC_FIELD_NUMBER: _ClassVar[int]
    FEHOKHCMJPD: _containers.RepeatedCompositeFieldContainer[_JIHHHAPKBEH_pb2.JIHHHAPKBEH]
    LFODPPNBHMN: _containers.RepeatedCompositeFieldContainer[_JIHHHAPKBEH_pb2.JIHHHAPKBEH]
    NCCPPHNNPBF: int
    OPHGAPAHHKC: _MGGAHFOAMJF_pb2.MGGAHFOAMJF
    def __init__(self, FEHOKHCMJPD: _Optional[_Iterable[_Union[_JIHHHAPKBEH_pb2.JIHHHAPKBEH, _Mapping]]] = ..., LFODPPNBHMN: _Optional[_Iterable[_Union[_JIHHHAPKBEH_pb2.JIHHHAPKBEH, _Mapping]]] = ..., NCCPPHNNPBF: _Optional[int] = ..., OPHGAPAHHKC: _Optional[_Union[_MGGAHFOAMJF_pb2.MGGAHFOAMJF, str]] = ...) -> None: ...
