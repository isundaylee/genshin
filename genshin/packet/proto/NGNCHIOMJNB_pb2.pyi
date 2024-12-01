from genshin.packet.proto import EEOPJGJJCPN_pb2 as _EEOPJGJJCPN_pb2
from genshin.packet.proto import ELFNOFGGCIA_pb2 as _ELFNOFGGCIA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NGNCHIOMJNB(_message.Message):
    __slots__ = ("EILAHBHKMED", "JAPEOEJLNPD", "ODCGIEDJAOJ", "LPJCHCADNPJ", "BNPDKNCPMCP", "HBIEMJBFNMP", "LICEOCKLOGD", "MCPPEKNBHFK")
    EILAHBHKMED_FIELD_NUMBER: _ClassVar[int]
    JAPEOEJLNPD_FIELD_NUMBER: _ClassVar[int]
    ODCGIEDJAOJ_FIELD_NUMBER: _ClassVar[int]
    LPJCHCADNPJ_FIELD_NUMBER: _ClassVar[int]
    BNPDKNCPMCP_FIELD_NUMBER: _ClassVar[int]
    HBIEMJBFNMP_FIELD_NUMBER: _ClassVar[int]
    LICEOCKLOGD_FIELD_NUMBER: _ClassVar[int]
    MCPPEKNBHFK_FIELD_NUMBER: _ClassVar[int]
    EILAHBHKMED: _containers.RepeatedCompositeFieldContainer[_EEOPJGJJCPN_pb2.EEOPJGJJCPN]
    JAPEOEJLNPD: int
    ODCGIEDJAOJ: bool
    LPJCHCADNPJ: bool
    BNPDKNCPMCP: bool
    HBIEMJBFNMP: int
    LICEOCKLOGD: _ELFNOFGGCIA_pb2.ELFNOFGGCIA
    MCPPEKNBHFK: int
    def __init__(self, EILAHBHKMED: _Optional[_Iterable[_Union[_EEOPJGJJCPN_pb2.EEOPJGJJCPN, _Mapping]]] = ..., JAPEOEJLNPD: _Optional[int] = ..., ODCGIEDJAOJ: bool = ..., LPJCHCADNPJ: bool = ..., BNPDKNCPMCP: bool = ..., HBIEMJBFNMP: _Optional[int] = ..., LICEOCKLOGD: _Optional[_Union[_ELFNOFGGCIA_pb2.ELFNOFGGCIA, str]] = ..., MCPPEKNBHFK: _Optional[int] = ...) -> None: ...
