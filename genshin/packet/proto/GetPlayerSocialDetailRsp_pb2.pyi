from genshin.packet.proto import SocialDetail_pb2 as _SocialDetail_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPlayerSocialDetailRsp(_message.Message):
    __slots__ = ("retcode", "detail_data")
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_DATA_FIELD_NUMBER: _ClassVar[int]
    retcode: int
    detail_data: _SocialDetail_pb2.SocialDetail
    def __init__(self, retcode: _Optional[int] = ..., detail_data: _Optional[_Union[_SocialDetail_pb2.SocialDetail, _Mapping]] = ...) -> None: ...
