from genshin.packet.proto import OKFHJLFOJEP_pb2 as _OKFHJLFOJEP_pb2
from genshin.packet.proto import DENADBADMPH_pb2 as _DENADBADMPH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LAADOJLABDH(_message.Message):
    __slots__ = ("PEMOIGKJAGH", "IOEEMCMLFHC", "FANIILAGPEA", "CDINGKPEACK", "JIJLDGMDIPF", "GLJELGNBEOJ")
    class IOEEMCMLFHCEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _DENADBADMPH_pb2.DENADBADMPH
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_DENADBADMPH_pb2.DENADBADMPH, _Mapping]] = ...) -> None: ...
    PEMOIGKJAGH_FIELD_NUMBER: _ClassVar[int]
    IOEEMCMLFHC_FIELD_NUMBER: _ClassVar[int]
    FANIILAGPEA_FIELD_NUMBER: _ClassVar[int]
    CDINGKPEACK_FIELD_NUMBER: _ClassVar[int]
    JIJLDGMDIPF_FIELD_NUMBER: _ClassVar[int]
    GLJELGNBEOJ_FIELD_NUMBER: _ClassVar[int]
    PEMOIGKJAGH: _OKFHJLFOJEP_pb2.OKFHJLFOJEP
    IOEEMCMLFHC: _containers.MessageMap[int, _DENADBADMPH_pb2.DENADBADMPH]
    FANIILAGPEA: _DENADBADMPH_pb2.DENADBADMPH
    CDINGKPEACK: int
    JIJLDGMDIPF: bool
    GLJELGNBEOJ: int
    def __init__(self, PEMOIGKJAGH: _Optional[_Union[_OKFHJLFOJEP_pb2.OKFHJLFOJEP, _Mapping]] = ..., IOEEMCMLFHC: _Optional[_Mapping[int, _DENADBADMPH_pb2.DENADBADMPH]] = ..., FANIILAGPEA: _Optional[_Union[_DENADBADMPH_pb2.DENADBADMPH, _Mapping]] = ..., CDINGKPEACK: _Optional[int] = ..., JIJLDGMDIPF: bool = ..., GLJELGNBEOJ: _Optional[int] = ...) -> None: ...
