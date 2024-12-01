from genshin.packet.proto import CAEIKHMPLFF_pb2 as _CAEIKHMPLFF_pb2
from genshin.packet.proto import LBMJMDNOOBO_pb2 as _LBMJMDNOOBO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LHPCCEMPKBB(_message.Message):
    __slots__ = ("PFNDPOBLJFO", "JCPBDGAJLEL", "PNDPNMBDOKF", "NOODCGKINAL")
    class NOODCGKINALEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PFNDPOBLJFO_FIELD_NUMBER: _ClassVar[int]
    JCPBDGAJLEL_FIELD_NUMBER: _ClassVar[int]
    PNDPNMBDOKF_FIELD_NUMBER: _ClassVar[int]
    NOODCGKINAL_FIELD_NUMBER: _ClassVar[int]
    PFNDPOBLJFO: _containers.RepeatedCompositeFieldContainer[_CAEIKHMPLFF_pb2.CAEIKHMPLFF]
    JCPBDGAJLEL: _containers.RepeatedCompositeFieldContainer[_CAEIKHMPLFF_pb2.CAEIKHMPLFF]
    PNDPNMBDOKF: _containers.RepeatedCompositeFieldContainer[_LBMJMDNOOBO_pb2.LBMJMDNOOBO]
    NOODCGKINAL: _containers.ScalarMap[int, int]
    def __init__(self, PFNDPOBLJFO: _Optional[_Iterable[_Union[_CAEIKHMPLFF_pb2.CAEIKHMPLFF, _Mapping]]] = ..., JCPBDGAJLEL: _Optional[_Iterable[_Union[_CAEIKHMPLFF_pb2.CAEIKHMPLFF, _Mapping]]] = ..., PNDPNMBDOKF: _Optional[_Iterable[_Union[_LBMJMDNOOBO_pb2.LBMJMDNOOBO, _Mapping]]] = ..., NOODCGKINAL: _Optional[_Mapping[int, int]] = ...) -> None: ...
