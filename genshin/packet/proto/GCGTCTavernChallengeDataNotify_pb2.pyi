from genshin.packet.proto import GCGTCTavernChallengeData_pb2 as _GCGTCTavernChallengeData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GCGTCTavernChallengeDataNotify(_message.Message):
    __slots__ = ("tavern_challenge_list",)
    TAVERN_CHALLENGE_LIST_FIELD_NUMBER: _ClassVar[int]
    tavern_challenge_list: _containers.RepeatedCompositeFieldContainer[_GCGTCTavernChallengeData_pb2.GCGTCTavernChallengeData]
    def __init__(self, tavern_challenge_list: _Optional[_Iterable[_Union[_GCGTCTavernChallengeData_pb2.GCGTCTavernChallengeData, _Mapping]]] = ...) -> None: ...
