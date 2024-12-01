from genshin.packet.proto import MEMAHNAJIBF_pb2 as _MEMAHNAJIBF_pb2
from genshin.packet.proto import MKBMDCGMIEO_pb2 as _MKBMDCGMIEO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJFHODJAFKF(_message.Message):
    __slots__ = ("AFIMMKIAPMH", "PPLMJPJOGCK", "KCMKCCCMMIO", "IGEAOBLJCJE", "JIPMFFLHKOM", "DKAOIABPLJM", "JAHPPELNEDF", "OOIPGFEDJMN", "HHMCFAIPPKB")
    class JIPMFFLHKOMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ...) -> None: ...
    AFIMMKIAPMH_FIELD_NUMBER: _ClassVar[int]
    PPLMJPJOGCK_FIELD_NUMBER: _ClassVar[int]
    KCMKCCCMMIO_FIELD_NUMBER: _ClassVar[int]
    IGEAOBLJCJE_FIELD_NUMBER: _ClassVar[int]
    JIPMFFLHKOM_FIELD_NUMBER: _ClassVar[int]
    DKAOIABPLJM_FIELD_NUMBER: _ClassVar[int]
    JAHPPELNEDF_FIELD_NUMBER: _ClassVar[int]
    OOIPGFEDJMN_FIELD_NUMBER: _ClassVar[int]
    HHMCFAIPPKB_FIELD_NUMBER: _ClassVar[int]
    AFIMMKIAPMH: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    PPLMJPJOGCK: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    KCMKCCCMMIO: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    IGEAOBLJCJE: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    JIPMFFLHKOM: _containers.MessageMap[int, _MEMAHNAJIBF_pb2.MEMAHNAJIBF]
    DKAOIABPLJM: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    JAHPPELNEDF: _containers.RepeatedCompositeFieldContainer[_MKBMDCGMIEO_pb2.MKBMDCGMIEO]
    OOIPGFEDJMN: int
    HHMCFAIPPKB: int
    def __init__(self, AFIMMKIAPMH: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., PPLMJPJOGCK: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., KCMKCCCMMIO: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., IGEAOBLJCJE: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., JIPMFFLHKOM: _Optional[_Mapping[int, _MEMAHNAJIBF_pb2.MEMAHNAJIBF]] = ..., DKAOIABPLJM: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., JAHPPELNEDF: _Optional[_Iterable[_Union[_MKBMDCGMIEO_pb2.MKBMDCGMIEO, _Mapping]]] = ..., OOIPGFEDJMN: _Optional[int] = ..., HHMCFAIPPKB: _Optional[int] = ...) -> None: ...
