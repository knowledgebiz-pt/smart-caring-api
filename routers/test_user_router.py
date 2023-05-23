import json
import internal
import requests


def test_fetch_user_id():
    second_validate = internal.validate_uuid.is_uuid_valid("123")
    validate = internal.validate_uuid.is_uuid_valid("1f58ff58-daa1-4e35-8910-5293d7667d40")
    assert validate is True
    assert second_validate is False