import os

import yaml

from portolano import portolano


def test_empty_repo():

    app = portolano()

    response = app.test_client().get('index.yaml')
    assert response.status_code == 200
    assert response.data == b"apiVersion: v1\nentries: {}\n"


def test_invalid_file_returns_404():

    app = portolano()
    response = app.test_client().get('foo.yaml')
    assert response.status_code == 404


def test_repo_with_chart(helm_chart):

    charts_path = helm_chart('foo')
    os.environ['CHARTS_FS_ROOT'] = charts_path
    app = portolano()

    response = app.test_client().get('index.yaml')
    assert response.status_code == 200
    data = yaml.load(response.data)
    assert len(data['entries']) == 1
    assert 'foo' in data['entries']
