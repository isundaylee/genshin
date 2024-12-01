from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LLGCDCDHDPD(_message.Message):
    __slots__ = ("JPLKHAPGPAO", "JAFFEMMJMKG", "KOADGMHFJBP", "IADKEMLAEAE", "KJOCAMIDMKB", "ICJNCAEDCLM")
    JPLKHAPGPAO_FIELD_NUMBER: _ClassVar[int]
    JAFFEMMJMKG_FIELD_NUMBER: _ClassVar[int]
    KOADGMHFJBP_FIELD_NUMBER: _ClassVar[int]
    IADKEMLAEAE_FIELD_NUMBER: _ClassVar[int]
    KJOCAMIDMKB_FIELD_NUMBER: _ClassVar[int]
    ICJNCAEDCLM_FIELD_NUMBER: _ClassVar[int]
    JPLKHAPGPAO: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    JAFFEMMJMKG: _JICKPPDLOHC_pb2.JICKPPDLOHC
    KOADGMHFJBP: int
    IADKEMLAEAE: int
    KJOCAMIDMKB: int
    ICJNCAEDCLM: int
    def __init__(self, JPLKHAPGPAO: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., JAFFEMMJMKG: _Optional[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]] = ..., KOADGMHFJBP: _Optional[int] = ..., IADKEMLAEAE: _Optional[int] = ..., KJOCAMIDMKB: _Optional[int] = ..., ICJNCAEDCLM: _Optional[int] = ...) -> None: ...
