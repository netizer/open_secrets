import open_secrets
from unittest import mock
from unittest.mock import patch
import json

@patch("open_secrets._default_project_id")
def test_get(mock__default_project_id):
    mock__default_project_id.return_value = False
    contents = {
        "SOME_KEY": "value"
    }
    json_contents = json.dumps(contents)
    with mock.patch("open_secrets.open", mock.mock_open(read_data=json_contents)) as m:
        result = open_secrets.get("SOME_KEY")
        assert result == "value"
