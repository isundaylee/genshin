from genshin.packet.proto import MEMAHNAJIBF_pb2 as _MEMAHNAJIBF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EBLCBLOFAHH(_message.Message):
    __slots__ = ("AFIMMKIAPMH", "IGEAOBLJCJE", "KCMKCCCMMIO", "JIPMFFLHKOM")
    class JIPMFFLHKOMEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ...) -> None: ...
    AFIMMKIAPMH_FIELD_NUMBER: _ClassVar[int]
    IGEAOBLJCJE_FIELD_NUMBER: _ClassVar[int]
    KCMKCCCMMIO_FIELD_NUMBER: _ClassVar[int]
    JIPMFFLHKOM_FIELD_NUMBER: _ClassVar[int]
    AFIMMKIAPMH: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    IGEAOBLJCJE: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    KCMKCCCMMIO: _MEMAHNAJIBF_pb2.MEMAHNAJIBF
    JIPMFFLHKOM: _containers.MessageMap[int, _MEMAHNAJIBF_pb2.MEMAHNAJIBF]
    def __init__(self, AFIMMKIAPMH: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., IGEAOBLJCJE: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., KCMKCCCMMIO: _Optional[_Union[_MEMAHNAJIBF_pb2.MEMAHNAJIBF, _Mapping]] = ..., JIPMFFLHKOM: _Optional[_Mapping[int, _MEMAHNAJIBF_pb2.MEMAHNAJIBF]] = ...) -> None: ...
