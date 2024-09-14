from genshin.packet.proto import InferenceWordInfo_pb2 as _InferenceWordInfo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InferencePageInfo(_message.Message):
    __slots__ = ("page_id", "unlock_word_list")
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_WORD_LIST_FIELD_NUMBER: _ClassVar[int]
    page_id: int
    unlock_word_list: _containers.RepeatedCompositeFieldContainer[_InferenceWordInfo_pb2.InferenceWordInfo]
    def __init__(self, page_id: _Optional[int] = ..., unlock_word_list: _Optional[_Iterable[_Union[_InferenceWordInfo_pb2.InferenceWordInfo, _Mapping]]] = ...) -> None: ...
