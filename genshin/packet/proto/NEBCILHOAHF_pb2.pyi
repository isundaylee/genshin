from genshin.packet.proto import IIHKHENLBCE_pb2 as _IIHKHENLBCE_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NEBCILHOAHF(_message.Message):
    __slots__ = ("EFHFPBEMMBG", "GKKLPKBPHNG", "PGFDGKFJHJI", "JCFLBHEHNNC", "LCLLNDINKKP")
    EFHFPBEMMBG_FIELD_NUMBER: _ClassVar[int]
    GKKLPKBPHNG_FIELD_NUMBER: _ClassVar[int]
    PGFDGKFJHJI_FIELD_NUMBER: _ClassVar[int]
    JCFLBHEHNNC_FIELD_NUMBER: _ClassVar[int]
    LCLLNDINKKP_FIELD_NUMBER: _ClassVar[int]
    EFHFPBEMMBG: _containers.RepeatedCompositeFieldContainer[_IIHKHENLBCE_pb2.IIHKHENLBCE]
    GKKLPKBPHNG: _containers.RepeatedCompositeFieldContainer[_IIHKHENLBCE_pb2.IIHKHENLBCE]
    PGFDGKFJHJI: int
    JCFLBHEHNNC: int
    LCLLNDINKKP: float
    def __init__(self, EFHFPBEMMBG: _Optional[_Iterable[_Union[_IIHKHENLBCE_pb2.IIHKHENLBCE, _Mapping]]] = ..., GKKLPKBPHNG: _Optional[_Iterable[_Union[_IIHKHENLBCE_pb2.IIHKHENLBCE, _Mapping]]] = ..., PGFDGKFJHJI: _Optional[int] = ..., JCFLBHEHNNC: _Optional[int] = ..., LCLLNDINKKP: _Optional[float] = ...) -> None: ...
