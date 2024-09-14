from genshin.packet.proto import InvestigationMonster_pb2 as _InvestigationMonster_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetInvestigationMonsterRsp(_message.Message):
    __slots__ = ("monster_list", "kis_for_mark", "retcode")
    MONSTER_LIST_FIELD_NUMBER: _ClassVar[int]
    KIS_FOR_MARK_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    monster_list: _containers.RepeatedCompositeFieldContainer[_InvestigationMonster_pb2.InvestigationMonster]
    kis_for_mark: bool
    retcode: int
    def __init__(self, monster_list: _Optional[_Iterable[_Union[_InvestigationMonster_pb2.InvestigationMonster, _Mapping]]] = ..., kis_for_mark: bool = ..., retcode: _Optional[int] = ...) -> None: ...
