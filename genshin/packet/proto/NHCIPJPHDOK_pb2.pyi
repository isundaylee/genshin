from genshin.packet.proto import EHBHODNNOCC_pb2 as _EHBHODNNOCC_pb2
from genshin.packet.proto import PBKKCEOCHEB_pb2 as _PBKKCEOCHEB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NHCIPJPHDOK(_message.Message):
    __slots__ = ("LANNAGNEIDJ", "PEOILIHAHJK", "IGBDOEBPPHO")
    LANNAGNEIDJ_FIELD_NUMBER: _ClassVar[int]
    PEOILIHAHJK_FIELD_NUMBER: _ClassVar[int]
    IGBDOEBPPHO_FIELD_NUMBER: _ClassVar[int]
    LANNAGNEIDJ: _containers.RepeatedCompositeFieldContainer[_EHBHODNNOCC_pb2.EHBHODNNOCC]
    PEOILIHAHJK: _containers.RepeatedCompositeFieldContainer[_PBKKCEOCHEB_pb2.PBKKCEOCHEB]
    IGBDOEBPPHO: int
    def __init__(self, LANNAGNEIDJ: _Optional[_Iterable[_Union[_EHBHODNNOCC_pb2.EHBHODNNOCC, _Mapping]]] = ..., PEOILIHAHJK: _Optional[_Iterable[_Union[_PBKKCEOCHEB_pb2.PBKKCEOCHEB, _Mapping]]] = ..., IGBDOEBPPHO: _Optional[int] = ...) -> None: ...
