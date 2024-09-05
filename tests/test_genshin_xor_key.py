from genshin.extensions import genshin_xor_key


def test_find_seed() -> None:
    """Test case matching the key in research/xor_key/test_key.txt"""
    assert genshin_xor_key.find_seed(0x79A8477626529AE3, 0x48927004912EFF74) == 0x123


def test_find_seed_invalid() -> None:
    """Test case matching the key in research/xor_key/test_key.txt"""
    assert genshin_xor_key.find_seed(0x0, 0x1) is None


def test_mt64() -> None:
    mt64 = genshin_xor_key.MT64(0x123)
    mt64.generate()

    assert mt64.generate() == 0x79A8477626529AE3
    assert mt64.generate() == 0x48927004912EFF74
