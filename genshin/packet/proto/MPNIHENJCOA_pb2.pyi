from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MPNIHENJCOA(_message.Message):
    __slots__ = ("HPBFOHOJKDH", "item_list", "MCMHEPOEOLD", "PJABEFAJBGB", "JIDJCMODOEA", "FKHKCPIMFKI", "BJLAGMAIDBI")
    HPBFOHOJKDH_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    MCMHEPOEOLD_FIELD_NUMBER: _ClassVar[int]
    PJABEFAJBGB_FIELD_NUMBER: _ClassVar[int]
    JIDJCMODOEA_FIELD_NUMBER: _ClassVar[int]
    FKHKCPIMFKI_FIELD_NUMBER: _ClassVar[int]
    BJLAGMAIDBI_FIELD_NUMBER: _ClassVar[int]
    HPBFOHOJKDH: _containers.RepeatedScalarFieldContainer[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    MCMHEPOEOLD: int
    PJABEFAJBGB: int
    JIDJCMODOEA: int
    FKHKCPIMFKI: bool
    BJLAGMAIDBI: int
    def __init__(self, HPBFOHOJKDH: _Optional[_Iterable[int]] = ..., item_list: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., MCMHEPOEOLD: _Optional[int] = ..., PJABEFAJBGB: _Optional[int] = ..., JIDJCMODOEA: _Optional[int] = ..., FKHKCPIMFKI: bool = ..., BJLAGMAIDBI: _Optional[int] = ...) -> None: ...
