from genshin.packet.proto import RegionSimpleInfo_pb2 as _RegionSimpleInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryRegionListHttpRsp(_message.Message):
    __slots__ = ("retcode", "region_list", "client_secret_key", "client_custom_config_encrypted", "enable_login_pc")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    REGION_LIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CUSTOM_CONFIG_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LOGIN_PC_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    region_list: _containers.RepeatedCompositeFieldContainer[_RegionSimpleInfo_pb2.RegionSimpleInfo]
    client_secret_key: bytes
    client_custom_config_encrypted: bytes
    enable_login_pc: bool
    def __init__(self, retcode: _Optional[int] = ..., region_list: _Optional[_Iterable[_Union[_RegionSimpleInfo_pb2.RegionSimpleInfo, _Mapping]]] = ..., client_secret_key: _Optional[bytes] = ..., client_custom_config_encrypted: _Optional[bytes] = ..., enable_login_pc: bool = ...) -> None: ...
