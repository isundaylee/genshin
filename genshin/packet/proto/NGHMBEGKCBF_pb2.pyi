from genshin.packet.proto import CKBMKLICBBO_pb2 as _CKBMKLICBBO_pb2
from genshin.packet.proto import LFJLGOJMKEH_pb2 as _LFJLGOJMKEH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NGHMBEGKCBF(_message.Message):
    __slots__ = ("GEKBOLFIBNK", "FFHPDCIBKOD", "IMIOGMDOKCB")
    GEKBOLFIBNK_FIELD_NUMBER: _ClassVar[int]
    FFHPDCIBKOD_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    GEKBOLFIBNK: _CKBMKLICBBO_pb2.CKBMKLICBBO
    FFHPDCIBKOD: int
    IMIOGMDOKCB: _LFJLGOJMKEH_pb2.LFJLGOJMKEH
    def __init__(self, GEKBOLFIBNK: _Optional[_Union[_CKBMKLICBBO_pb2.CKBMKLICBBO, _Mapping]] = ..., FFHPDCIBKOD: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_LFJLGOJMKEH_pb2.LFJLGOJMKEH, str]] = ...) -> None: ...
