import os

import yaml

from portolano import portolano


def test_upload_must_have_file():

    app = portolano()
    response = app.test_client().post(
        '/charts/',
    )

    assert response.status_code == 400


def test_upload_helm_chart(tmpdir, helm_chart):

    chart_path = helm_chart("foo")
    chart_archive = os.path.join(chart_path, "foo-0.1.0.tgz")

    repo_dir = tmpdir.mkdtemp()
    with repo_dir.as_cwd():
        os.environ['CHARTS_FS_URL'] = "http://bar.com"

        app = portolano()
        with open(chart_archive, 'rb') as chart_file:
            response = app.test_client().post(
                '/charts/',
                data={
                    'file': chart_file
                }
            )

        assert response.status_code == 200

        response = app.test_client().get('index.yaml')
        data = yaml.load(response.data)
        assert data['entries']['foo'][0]['urls'][0] == 'http://bar.com/foo-0.1.0.tgz'


