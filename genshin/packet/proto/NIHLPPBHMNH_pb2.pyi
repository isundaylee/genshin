from genshin.packet.proto import EJPDLPLCAJH_pb2 as _EJPDLPLCAJH_pb2
from genshin.packet.proto import EKFGGHCLOMJ_pb2 as _EKFGGHCLOMJ_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NIHLPPBHMNH(_message.Message):
    __slots__ = ("DHEGCBCHMMJ", "CCENDAMKOEM", "BPJDJDFFKDH", "KLMDAPCLGAP")
    DHEGCBCHMMJ_FIELD_NUMBER: _ClassVar[int]
    CCENDAMKOEM_FIELD_NUMBER: _ClassVar[int]
    BPJDJDFFKDH_FIELD_NUMBER: _ClassVar[int]
    KLMDAPCLGAP_FIELD_NUMBER: _ClassVar[int]
    DHEGCBCHMMJ: _EJPDLPLCAJH_pb2.EJPDLPLCAJH
    CCENDAMKOEM: _EKFGGHCLOMJ_pb2.EKFGGHCLOMJ
    BPJDJDFFKDH: int
    KLMDAPCLGAP: int
    def __init__(self, DHEGCBCHMMJ: _Optional[_Union[_EJPDLPLCAJH_pb2.EJPDLPLCAJH, _Mapping]] = ..., CCENDAMKOEM: _Optional[_Union[_EKFGGHCLOMJ_pb2.EKFGGHCLOMJ, _Mapping]] = ..., BPJDJDFFKDH: _Optional[int] = ..., KLMDAPCLGAP: _Optional[int] = ...) -> None: ...
