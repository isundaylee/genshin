from genshin.packet.proto import EKGHDLKKKPO_pb2 as _EKGHDLKKKPO_pb2
from genshin.packet.proto import HPBCMBFEKGO_pb2 as _HPBCMBFEKGO_pb2
from genshin.packet.proto import LJDOIFMJABA_pb2 as _LJDOIFMJABA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GPBHBCBEHKI(_message.Message):
    __slots__ = ("EMDKFPHKAHC", "ELFDJMAFEMP", "DBBBAKDKDNC")
    EMDKFPHKAHC_FIELD_NUMBER: _ClassVar[int]
    ELFDJMAFEMP_FIELD_NUMBER: _ClassVar[int]
    DBBBAKDKDNC_FIELD_NUMBER: _ClassVar[int]
    EMDKFPHKAHC: _EKGHDLKKKPO_pb2.EKGHDLKKKPO
    ELFDJMAFEMP: _HPBCMBFEKGO_pb2.HPBCMBFEKGO
    DBBBAKDKDNC: _LJDOIFMJABA_pb2.LJDOIFMJABA
    def __init__(self, EMDKFPHKAHC: _Optional[_Union[_EKGHDLKKKPO_pb2.EKGHDLKKKPO, _Mapping]] = ..., ELFDJMAFEMP: _Optional[_Union[_HPBCMBFEKGO_pb2.HPBCMBFEKGO, _Mapping]] = ..., DBBBAKDKDNC: _Optional[_Union[_LJDOIFMJABA_pb2.LJDOIFMJABA, _Mapping]] = ...) -> None: ...
