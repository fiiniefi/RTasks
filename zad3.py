import requests
import json
import pytest


URL = 'https://prod-117.westeurope.logic.azure.com/workflows/39f4228d572b4c43bc199509cae51412/triggers/manual/' \
      'paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=' \
      '2LYFWu0uKzekrgt83e1hIy547fIDvTb3v0WAfk2yyj4'


@pytest.fixture()
def headers():
    return {'Content-Type': 'application/json'}


@pytest.fixture(scope='function')
def payload(request):
    return {'a': request.param[0], 'b': request.param[1]}


@pytest.mark.parametrize("payload", [(2, 0), ("wrong", "args")], indirect=['payload'])
def test_InvalidArgs_RaisesBadRequest(headers, payload):
    result = requests.post(url=URL, data=json.dumps(payload), headers=headers)
    assert result.status_code == 400


def test_InvalidRestMethod_RaisesBadRequest(headers):
    result = requests.get(url=URL, headers=headers)
    assert result.status_code == 400





@pytest.mark.parametrize("payload", [(10, 5)], indirect=['payload'])
def test_does_sth(headers, payload):
    result = requests.post(url=URL, data=json.dumps(payload), headers=headers)
    print(result.text)
