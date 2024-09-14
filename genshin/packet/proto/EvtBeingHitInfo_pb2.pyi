from genshin.packet.proto import AttackResult_pb2 as _AttackResult_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvtBeingHitInfo(_message.Message):
    __slots__ = ("frame_num", "peer_id", "attack_result")
    FRAME_NUM_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACK_RESULT_FIELD_NUMBER: _ClassVar[int]
    frame_num: int
    peer_id: int
    attack_result: _AttackResult_pb2.AttackResult
    def __init__(self, frame_num: _Optional[int] = ..., peer_id: _Optional[int] = ..., attack_result: _Optional[_Union[_AttackResult_pb2.AttackResult, _Mapping]] = ...) -> None: ...
