from genshin.packet.proto import InvestigationTarget_pb2 as _InvestigationTarget_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerInvestigationTargetNotify(_message.Message):
    __slots__ = ("investigation_target_list",)
    INVESTIGATION_TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    investigation_target_list: _containers.RepeatedCompositeFieldContainer[_InvestigationTarget_pb2.InvestigationTarget]
    def __init__(self, investigation_target_list: _Optional[_Iterable[_Union[_InvestigationTarget_pb2.InvestigationTarget, _Mapping]]] = ...) -> None: ...
