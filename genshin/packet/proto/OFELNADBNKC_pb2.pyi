from genshin.packet.proto import PPAICMKDNEI_pb2 as _PPAICMKDNEI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OFELNADBNKC(_message.Message):
    __slots__ = ("EPFCIDIKLKG", "AJMMAEEGJEA", "CJPDFHODJGO", "POGDPFNPMDB", "HLBECOIBPBP", "MHENBJCACME")
    EPFCIDIKLKG_FIELD_NUMBER: _ClassVar[int]
    AJMMAEEGJEA_FIELD_NUMBER: _ClassVar[int]
    CJPDFHODJGO_FIELD_NUMBER: _ClassVar[int]
    POGDPFNPMDB_FIELD_NUMBER: _ClassVar[int]
    HLBECOIBPBP_FIELD_NUMBER: _ClassVar[int]
    MHENBJCACME_FIELD_NUMBER: _ClassVar[int]
    EPFCIDIKLKG: int
    AJMMAEEGJEA: int
    CJPDFHODJGO: int
    POGDPFNPMDB: _PPAICMKDNEI_pb2.PPAICMKDNEI
    HLBECOIBPBP: int
    MHENBJCACME: int
    def __init__(self, EPFCIDIKLKG: _Optional[int] = ..., AJMMAEEGJEA: _Optional[int] = ..., CJPDFHODJGO: _Optional[int] = ..., POGDPFNPMDB: _Optional[_Union[_PPAICMKDNEI_pb2.PPAICMKDNEI, str]] = ..., HLBECOIBPBP: _Optional[int] = ..., MHENBJCACME: _Optional[int] = ...) -> None: ...
