from genshin.packet.proto import HALJNIJMECG_pb2 as _HALJNIJMECG_pb2
from genshin.packet.proto import DPBLGHLGGKI_pb2 as _DPBLGHLGGKI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AMLAJJBGFIJ(_message.Message):
    __slots__ = ("ENNBCJCMCNH", "BJBHOMMGPOK", "GCBGBFAGBIM", "BOFFIDCGJEM", "CFNKIAEELHN")
    ENNBCJCMCNH_FIELD_NUMBER: _ClassVar[int]
    BJBHOMMGPOK_FIELD_NUMBER: _ClassVar[int]
    GCBGBFAGBIM_FIELD_NUMBER: _ClassVar[int]
    BOFFIDCGJEM_FIELD_NUMBER: _ClassVar[int]
    CFNKIAEELHN_FIELD_NUMBER: _ClassVar[int]
    ENNBCJCMCNH: _containers.RepeatedCompositeFieldContainer[_HALJNIJMECG_pb2.HALJNIJMECG]
    BJBHOMMGPOK: _containers.RepeatedCompositeFieldContainer[_DPBLGHLGGKI_pb2.DPBLGHLGGKI]
    GCBGBFAGBIM: bool
    BOFFIDCGJEM: int
    CFNKIAEELHN: int
    def __init__(self, ENNBCJCMCNH: _Optional[_Iterable[_Union[_HALJNIJMECG_pb2.HALJNIJMECG, _Mapping]]] = ..., BJBHOMMGPOK: _Optional[_Iterable[_Union[_DPBLGHLGGKI_pb2.DPBLGHLGGKI, _Mapping]]] = ..., GCBGBFAGBIM: bool = ..., BOFFIDCGJEM: _Optional[int] = ..., CFNKIAEELHN: _Optional[int] = ...) -> None: ...
