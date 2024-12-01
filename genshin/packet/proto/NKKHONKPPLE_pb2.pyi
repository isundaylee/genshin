from genshin.packet.proto import DCIHCIPIODA_pb2 as _DCIHCIPIODA_pb2
from genshin.packet.proto import LMJBPCIGOBK_pb2 as _LMJBPCIGOBK_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NKKHONKPPLE(_message.Message):
    __slots__ = ("NCMGBIGFFLG", "BNGPKPJNMCG")
    NCMGBIGFFLG_FIELD_NUMBER: _ClassVar[int]
    BNGPKPJNMCG_FIELD_NUMBER: _ClassVar[int]
    NCMGBIGFFLG: _DCIHCIPIODA_pb2.DCIHCIPIODA
    BNGPKPJNMCG: _LMJBPCIGOBK_pb2.LMJBPCIGOBK
    def __init__(self, NCMGBIGFFLG: _Optional[_Union[_DCIHCIPIODA_pb2.DCIHCIPIODA, _Mapping]] = ..., BNGPKPJNMCG: _Optional[_Union[_LMJBPCIGOBK_pb2.LMJBPCIGOBK, str]] = ...) -> None: ...
