from genshin.packet.proto import LJJFJILBNLL_pb2 as _LJJFJILBNLL_pb2
from genshin.packet.proto import JICKPPDLOHC_pb2 as _JICKPPDLOHC_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KDPJDHAJKAN(_message.Message):
    __slots__ = ("ICCHDGKMNLF", "JBPHCHJPDEM", "EMPEJFOGNPA", "MIOLBJEPFGP", "EJNINFFFKJP")
    ICCHDGKMNLF_FIELD_NUMBER: _ClassVar[int]
    JBPHCHJPDEM_FIELD_NUMBER: _ClassVar[int]
    EMPEJFOGNPA_FIELD_NUMBER: _ClassVar[int]
    MIOLBJEPFGP_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    ICCHDGKMNLF: _LJJFJILBNLL_pb2.LJJFJILBNLL
    JBPHCHJPDEM: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    EMPEJFOGNPA: _containers.RepeatedCompositeFieldContainer[_JICKPPDLOHC_pb2.JICKPPDLOHC]
    MIOLBJEPFGP: int
    EJNINFFFKJP: int
    def __init__(self, ICCHDGKMNLF: _Optional[_Union[_LJJFJILBNLL_pb2.LJJFJILBNLL, _Mapping]] = ..., JBPHCHJPDEM: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., EMPEJFOGNPA: _Optional[_Iterable[_Union[_JICKPPDLOHC_pb2.JICKPPDLOHC, _Mapping]]] = ..., MIOLBJEPFGP: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
