from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(None, 1)
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('None', 'B')

    reverse = encrypt_message('batata', 99)
    assert reverse == 'atatab'

    even = encrypt_message('abcdef', 4)
    assert even == 'fe_dcba'

    odd = encrypt_message('abcdef', 3)
    assert odd == 'cba_fed'