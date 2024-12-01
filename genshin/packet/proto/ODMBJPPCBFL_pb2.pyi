from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import LIGDIKNFKJC_pb2 as _LIGDIKNFKJC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ODMBJPPCBFL(_message.Message):
    __slots__ = ("JHBCBIEOBEP", "AEGCOGAHFGI", "LKAJMMFHNDH", "HGPNDHKDGDO", "GJMPBCHFKLH", "EJNINFFFKJP")
    JHBCBIEOBEP_FIELD_NUMBER: _ClassVar[int]
    AEGCOGAHFGI_FIELD_NUMBER: _ClassVar[int]
    LKAJMMFHNDH_FIELD_NUMBER: _ClassVar[int]
    HGPNDHKDGDO_FIELD_NUMBER: _ClassVar[int]
    GJMPBCHFKLH_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    JHBCBIEOBEP: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    AEGCOGAHFGI: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    LKAJMMFHNDH: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    HGPNDHKDGDO: bool
    GJMPBCHFKLH: _LIGDIKNFKJC_pb2.LIGDIKNFKJC
    EJNINFFFKJP: int
    def __init__(self, JHBCBIEOBEP: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., AEGCOGAHFGI: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., LKAJMMFHNDH: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., HGPNDHKDGDO: bool = ..., GJMPBCHFKLH: _Optional[_Union[_LIGDIKNFKJC_pb2.LIGDIKNFKJC, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
