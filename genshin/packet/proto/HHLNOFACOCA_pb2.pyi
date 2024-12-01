from genshin.packet.proto import HFHJKHOPLMN_pb2 as _HFHJKHOPLMN_pb2
from genshin.packet.proto import LLCCBEANIFC_pb2 as _LLCCBEANIFC_pb2
from genshin.packet.proto import LFJLGOJMKEH_pb2 as _LFJLGOJMKEH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HHLNOFACOCA(_message.Message):
    __slots__ = ("MEIKGBOLDGH", "FAGJDJIGLON", "ABIMANELKOC", "IMIOGMDOKCB", "OMENIAMEDCE")
    MEIKGBOLDGH_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    ABIMANELKOC_FIELD_NUMBER: _ClassVar[int]
    IMIOGMDOKCB_FIELD_NUMBER: _ClassVar[int]
    OMENIAMEDCE_FIELD_NUMBER: _ClassVar[int]
    MEIKGBOLDGH: _containers.RepeatedCompositeFieldContainer[_HFHJKHOPLMN_pb2.HFHJKHOPLMN]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_LLCCBEANIFC_pb2.LLCCBEANIFC]
    ABIMANELKOC: int
    IMIOGMDOKCB: _LFJLGOJMKEH_pb2.LFJLGOJMKEH
    OMENIAMEDCE: bool
    def __init__(self, MEIKGBOLDGH: _Optional[_Iterable[_Union[_HFHJKHOPLMN_pb2.HFHJKHOPLMN, _Mapping]]] = ..., FAGJDJIGLON: _Optional[_Iterable[_Union[_LLCCBEANIFC_pb2.LLCCBEANIFC, _Mapping]]] = ..., ABIMANELKOC: _Optional[int] = ..., IMIOGMDOKCB: _Optional[_Union[_LFJLGOJMKEH_pb2.LFJLGOJMKEH, str]] = ..., OMENIAMEDCE: bool = ...) -> None: ...
