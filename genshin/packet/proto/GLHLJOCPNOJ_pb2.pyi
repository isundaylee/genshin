from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from genshin.packet.proto import MBJEPLKJNIG_pb2 as _MBJEPLKJNIG_pb2
from genshin.packet.proto import MHJJGCMMGLO_pb2 as _MHJJGCMMGLO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GLHLJOCPNOJ(_message.Message):
    __slots__ = ("PCPCBEBALLB", "AAFLLAHKNJE", "JFONAHFNHKA", "EJNINFFFKJP")
    PCPCBEBALLB_FIELD_NUMBER: _ClassVar[int]
    AAFLLAHKNJE_FIELD_NUMBER: _ClassVar[int]
    JFONAHFNHKA_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    PCPCBEBALLB: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    AAFLLAHKNJE: _containers.RepeatedCompositeFieldContainer[_MBJEPLKJNIG_pb2.MBJEPLKJNIG]
    JFONAHFNHKA: _MHJJGCMMGLO_pb2.MHJJGCMMGLO
    EJNINFFFKJP: int
    def __init__(self, PCPCBEBALLB: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., AAFLLAHKNJE: _Optional[_Iterable[_Union[_MBJEPLKJNIG_pb2.MBJEPLKJNIG, _Mapping]]] = ..., JFONAHFNHKA: _Optional[_Union[_MHJJGCMMGLO_pb2.MHJJGCMMGLO, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
