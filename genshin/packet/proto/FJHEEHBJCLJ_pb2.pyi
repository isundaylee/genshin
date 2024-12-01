from genshin.packet.proto import ABAGANPIOID_pb2 as _ABAGANPIOID_pb2
from genshin.packet.proto import KHHLGFEHBGJ_pb2 as _KHHLGFEHBGJ_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FJHEEHBJCLJ(_message.Message):
    __slots__ = ("OEOOHDALNCE", "IEDDMDENJAA", "JAHPPELNEDF", "KCPBCOLPBME", "AKJCCMMODMM", "MEMIAFJCJOK")
    OEOOHDALNCE_FIELD_NUMBER: _ClassVar[int]
    IEDDMDENJAA_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    KCPBCOLPBME_FIELD_NUMBER: _ClassVar[int]
    AKJCCMMODMM_FIELD_NUMBER: _ClassVar[int]
    MEMIAFJCJOK_FIELD_NUMBER: _ClassVar[int]
    OEOOHDALNCE: _containers.RepeatedCompositeFieldContainer[_ABAGANPIOID_pb2.ABAGANPIOID]
    IEDDMDENJAA: _containers.RepeatedScalarFieldContainer[int]
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_KHHLGFEHBGJ_pb2.KHHLGFEHBGJ]
    KCPBCOLPBME: _containers.RepeatedScalarFieldContainer[int]
    AKJCCMMODMM: _containers.RepeatedScalarFieldContainer[int]
    MEMIAFJCJOK: int
    def __init__(self, OEOOHDALNCE: _Optional[_Iterable[_Union[_ABAGANPIOID_pb2.ABAGANPIOID, _Mapping]]] = ..., IEDDMDENJAA: _Optional[_Iterable[int]] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_KHHLGFEHBGJ_pb2.KHHLGFEHBGJ, _Mapping]]] = ..., KCPBCOLPBME: _Optional[_Iterable[int]] = ..., AKJCCMMODMM: _Optional[_Iterable[int]] = ..., MEMIAFJCJOK: _Optional[int] = ...) -> None: ...
