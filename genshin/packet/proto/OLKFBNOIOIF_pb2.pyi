from genshin.packet.proto import DHDEBBIPIIF_pb2 as _DHDEBBIPIIF_pb2
from genshin.packet.proto import PODKLCCMDID_pb2 as _PODKLCCMDID_pb2
from genshin.packet.proto import NPPKGKLHLOD_pb2 as _NPPKGKLHLOD_pb2
from genshin.packet.proto import NLCHENONCBI_pb2 as _NLCHENONCBI_pb2
from genshin.packet.proto import OAAFLEBINLN_pb2 as _OAAFLEBINLN_pb2
from genshin.packet.proto import LLPEEGBJOFA_pb2 as _LLPEEGBJOFA_pb2
from genshin.packet.proto import GDMJGBFBFHP_pb2 as _GDMJGBFBFHP_pb2
from genshin.packet.proto import GKNMALEJKHN_pb2 as _GKNMALEJKHN_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OLKFBNOIOIF(_message.Message):
    __slots__ = ("CKEHABLGHNN", "MPNJAOCKMAH", "fairy_tales_flyppy_hat_info", "bird_ball_client_info", "ceremony_doodle_info", "catcafe_info", "great_festival_v2_sheet_restore_info", "float_toy_info", "cook_game_info", "FINAHGLFHAG", "JCHHJFLDLGA")
    CKEHABLGHNN_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    FAIRY_TALES_FLYPPY_HAT_INFO_FIELD_NUMBER: _ClassVar[int]
    BIRD_BALL_CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    CEREMONY_DOODLE_INFO_FIELD_NUMBER: _ClassVar[int]
    CATCAFE_INFO_FIELD_NUMBER: _ClassVar[int]
    GREAT_FESTIVAL_V2_SHEET_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    FLOAT_TOY_INFO_FIELD_NUMBER: _ClassVar[int]
    COOK_GAME_INFO_FIELD_NUMBER: _ClassVar[int]
    FINAHGLFHAG_FIELD_NUMBER: _ClassVar[int]
    JCHHJFLDLGA_FIELD_NUMBER: _ClassVar[int]
    CKEHABLGHNN: _DHDEBBIPIIF_pb2.DHDEBBIPIIF
    MPNJAOCKMAH: int
    fairy_tales_flyppy_hat_info: _PODKLCCMDID_pb2.PODKLCCMDID
    bird_ball_client_info: _NPPKGKLHLOD_pb2.NPPKGKLHLOD
    ceremony_doodle_info: _NLCHENONCBI_pb2.NLCHENONCBI
    catcafe_info: _OAAFLEBINLN_pb2.OAAFLEBINLN
    great_festival_v2_sheet_restore_info: _LLPEEGBJOFA_pb2.LLPEEGBJOFA
    float_toy_info: _GDMJGBFBFHP_pb2.GDMJGBFBFHP
    cook_game_info: _GKNMALEJKHN_pb2.GKNMALEJKHN
    FINAHGLFHAG: int
    JCHHJFLDLGA: bool
    def __init__(self, CKEHABLGHNN: _Optional[_Union[_DHDEBBIPIIF_pb2.DHDEBBIPIIF, str]] = ..., MPNJAOCKMAH: _Optional[int] = ..., fairy_tales_flyppy_hat_info: _Optional[_Union[_PODKLCCMDID_pb2.PODKLCCMDID, _Mapping]] = ..., bird_ball_client_info: _Optional[_Union[_NPPKGKLHLOD_pb2.NPPKGKLHLOD, _Mapping]] = ..., ceremony_doodle_info: _Optional[_Union[_NLCHENONCBI_pb2.NLCHENONCBI, _Mapping]] = ..., catcafe_info: _Optional[_Union[_OAAFLEBINLN_pb2.OAAFLEBINLN, _Mapping]] = ..., great_festival_v2_sheet_restore_info: _Optional[_Union[_LLPEEGBJOFA_pb2.LLPEEGBJOFA, _Mapping]] = ..., float_toy_info: _Optional[_Union[_GDMJGBFBFHP_pb2.GDMJGBFBFHP, _Mapping]] = ..., cook_game_info: _Optional[_Union[_GKNMALEJKHN_pb2.GKNMALEJKHN, _Mapping]] = ..., FINAHGLFHAG: _Optional[int] = ..., JCHHJFLDLGA: bool = ...) -> None: ...
