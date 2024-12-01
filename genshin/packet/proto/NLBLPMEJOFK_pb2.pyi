from genshin.packet.proto import ODFNOHDICEC_pb2 as _ODFNOHDICEC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NLBLPMEJOFK(_message.Message):
    __slots__ = ("LFIJOMFAAGJ", "KKPIDNFHGCJ", "LDGNPKGAMFJ", "PFBMHAFNGBM")
    LFIJOMFAAGJ_FIELD_NUMBER: _ClassVar[int]
    KKPIDNFHGCJ_FIELD_NUMBER: _ClassVar[int]
    LDGNPKGAMFJ_FIELD_NUMBER: _ClassVar[int]
    PFBMHAFNGBM_FIELD_NUMBER: _ClassVar[int]
    LFIJOMFAAGJ: _containers.RepeatedCompositeFieldContainer[_ODFNOHDICEC_pb2.ODFNOHDICEC]
    KKPIDNFHGCJ: bool
    LDGNPKGAMFJ: bool
    PFBMHAFNGBM: int
    def __init__(self, LFIJOMFAAGJ: _Optional[_Iterable[_Union[_ODFNOHDICEC_pb2.ODFNOHDICEC, _Mapping]]] = ..., KKPIDNFHGCJ: bool = ..., LDGNPKGAMFJ: bool = ..., PFBMHAFNGBM: _Optional[int] = ...) -> None: ...
