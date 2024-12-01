from genshin.packet.proto import HKIHLAEPCPL_pb2 as _HKIHLAEPCPL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MHOJPFGMMHL(_message.Message):
    __slots__ = ("PJNIMNLMIOP", "EAIPGEMKNPO", "IEJPGHNLIDB", "EPIENMJEHFO", "BDCBLNLCAGE", "GLKNGDDNOCN")
    class PJNIMNLMIOPEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _HKIHLAEPCPL_pb2.HKIHLAEPCPL
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_HKIHLAEPCPL_pb2.HKIHLAEPCPL, _Mapping]] = ...) -> None: ...
    PJNIMNLMIOP_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    IEJPGHNLIDB_FIELD_NUMBER: _ClassVar[int]
    EPIENMJEHFO_FIELD_NUMBER: _ClassVar[int]
    BDCBLNLCAGE_FIELD_NUMBER: _ClassVar[int]
    GLKNGDDNOCN_FIELD_NUMBER: _ClassVar[int]
    PJNIMNLMIOP: _containers.MessageMap[int, _HKIHLAEPCPL_pb2.HKIHLAEPCPL]
    EAIPGEMKNPO: int
    IEJPGHNLIDB: int
    EPIENMJEHFO: int
    BDCBLNLCAGE: bool
    GLKNGDDNOCN: bool
    def __init__(self, PJNIMNLMIOP: _Optional[_Mapping[int, _HKIHLAEPCPL_pb2.HKIHLAEPCPL]] = ..., EAIPGEMKNPO: _Optional[int] = ..., IEJPGHNLIDB: _Optional[int] = ..., EPIENMJEHFO: _Optional[int] = ..., BDCBLNLCAGE: bool = ..., GLKNGDDNOCN: bool = ...) -> None: ...
