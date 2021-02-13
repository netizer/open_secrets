from open_secrets import get
from unittest import mock
from unittest.mock import patch
import json

@patch("open_secrets.has_env_var")
def test_get(mock_has_env_var):
    mock_has_env_var.return_value = False
    contents = {
        "SOME_KEY": "value"
    }
    json_contents = json.dumps(contents)
    with mock.patch("open_secrets.open", mock.mock_open(read_data=json_contents)) as m:
        assert get("SOME_KEY") == "value"
