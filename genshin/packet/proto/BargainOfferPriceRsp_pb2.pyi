from genshin.packet.proto import BargainResultType_pb2 as _BargainResultType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BargainOfferPriceRsp(_message.Message):
    __slots__ = ("cur_mood", "result_param", "bargain_result", "retcode")
    CUR_MOOD_FIELD_NUMBER: _ClassVar[int]
    RESULT_PARAM_FIELD_NUMBER: _ClassVar[int]
    BARGAIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    cur_mood: int
    result_param: int
    bargain_result: _BargainResultType_pb2.BargainResultType
    retcode: int
    def __init__(self, cur_mood: _Optional[int] = ..., result_param: _Optional[int] = ..., bargain_result: _Optional[_Union[_BargainResultType_pb2.BargainResultType, str]] = ..., retcode: _Optional[int] = ...) -> None: ...
