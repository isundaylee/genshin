from genshin.packet.proto import DEIGILFODBD_pb2 as _DEIGILFODBD_pb2
from genshin.packet.proto import GPKBOBCLBCL_pb2 as _GPKBOBCLBCL_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MLNLCBOMDHG(_message.Message):
    __slots__ = ("HGDGJJFBFND", "GGGNJBEIJOG", "IMIOGMDOKCB")
    HGDGJJFBFND_FIELD_NUMBER: _ClassVar[int]
    GGGNJBEIJOG_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    HGDGJJFBFND: _DEIGILFODBD_pb2.DEIGILFODBD
    GGGNJBEIJOG: bool
    IMIOGMDOKCB: _GPKBOBCLBCL_pb2.GPKBOBCLBCL
    def __init__(self, HGDGJJFBFND: _Optional[_Union[_DEIGILFODBD_pb2.DEIGILFODBD, _Mapping]] = ..., GGGNJBEIJOG: bool = ..., IMIOGMDOKCB: _Optional[_Union[_GPKBOBCLBCL_pb2.GPKBOBCLBCL, str]] = ...) -> None: ...
