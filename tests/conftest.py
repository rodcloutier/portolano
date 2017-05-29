import os
import subprocess

import pytest

from portolano import helm


@pytest.fixture
def helm_chart(tmpdir):

    def create(chart_name):
        temp_path = tmpdir.mkdtemp()

        with temp_path.as_cwd():
            subprocess.run(['helm', 'create', chart_name])

            chart_path = temp_path.join(chart_name)

            chart_path.chdir()
            subprocess.run(['helm', 'package', '.'])
            archive_name = 'foo-0.1.0.tgz'
            helm.process(archive_name, "file://")

        return os.path.join(chart_path.dirname, chart_path.basename)
    return create
