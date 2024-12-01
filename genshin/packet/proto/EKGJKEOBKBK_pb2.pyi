from genshin.packet.proto import JOECDAOLNFD_pb2 as _JOECDAOLNFD_pb2
from genshin.packet.proto import IDLAEJGILNL_pb2 as _IDLAEJGILNL_pb2
from genshin.packet.proto import HFILDBLLMOP_pb2 as _HFILDBLLMOP_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EKGJKEOBKBK(_message.Message):
    __slots__ = ("KFIIICLOLKG", "NABHBHGBPON", "GAFMCJBMFAE")
    KFIIICLOLKG_FIELD_NUMBER: _ClassVar[int]
    NABHBHGBPON_FIELD_NUMBER: _ClassVar[int]
    GAFMCJBMFAE_FIELD_NUMBER: _ClassVar[int]
    KFIIICLOLKG: _JOECDAOLNFD_pb2.JOECDAOLNFD
    NABHBHGBPON: _IDLAEJGILNL_pb2.IDLAEJGILNL
    GAFMCJBMFAE: _HFILDBLLMOP_pb2.HFILDBLLMOP
    def __init__(self, KFIIICLOLKG: _Optional[_Union[_JOECDAOLNFD_pb2.JOECDAOLNFD, _Mapping]] = ..., NABHBHGBPON: _Optional[_Union[_IDLAEJGILNL_pb2.IDLAEJGILNL, _Mapping]] = ..., GAFMCJBMFAE: _Optional[_Union[_HFILDBLLMOP_pb2.HFILDBLLMOP, _Mapping]] = ...) -> None: ...
