from survey_fix import *

import pytest
from click.testing import CliRunner


@pytest.mark.parametrize("a, b, expected", [
    ([0, 0, 0], [0, 0, 1], 1),
    ([0, 0], [0, 1], 1),
    ([1, 0], [0, 1], sqrt(2)),
])
def test_dist(a, b, expected):
    assert dist(a, b) == expected


def test_main(tmpdir):
    infile = str(tmpdir.join("in.dxf"))
    with r12writer(infile) as dxf:
        points = [(1, 0, 0), (2, 0, 0), (3, 0, 0)]
        texts = [
            ((1.1, 0), 'foo'),
            ((2, 0.1), '8'),
            ((3, 0.1), '6.3'),
        ]

        for pt in points:
            dxf.add_point(pt)
        for pt, txt in texts:
            dxf.add_text(txt, insert=pt)

    outfile = str(tmpdir.join("out.dxf"))

    runner = CliRunner()
    r = runner.invoke(main, [infile, outfile])
    assert r.exit_code == 0

    dxf = ezdxf.readfile(str(outfile))
    locations = [e.get_dxf_attrib('location') for e in dxf.modelspace()]
    expected = [(2, 0, 8), (3, 0, 6.3)]
    assert locations == expected
