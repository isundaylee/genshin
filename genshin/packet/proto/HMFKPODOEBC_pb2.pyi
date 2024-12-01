from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HMFKPODOEBC(_message.Message):
    __slots__ = ("BNJOJBOPMFJ", "ANHCGHNLBNE", "ADJNOLPLKOA")
    class ANHCGHNLBNEEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BNJOJBOPMFJ_FIELD_NUMBER: _ClassVar[int]
    ANHCGHNLBNE_FIELD_NUMBER: _ClassVar[int]
    ADJNOLPLKOA_FIELD_NUMBER: _ClassVar[int]
    BNJOJBOPMFJ: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    ANHCGHNLBNE: _containers.ScalarMap[int, int]
    ADJNOLPLKOA: int
    def __init__(self, BNJOJBOPMFJ: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., ANHCGHNLBNE: _Optional[_Mapping[int, int]] = ..., ADJNOLPLKOA: _Optional[int] = ...) -> None: ...
