import ezdxf
from ezdxf.r12writer import r12writer
import click
from pathlib import Path
import operator as op
from math import sqrt


def dist(a, b):
    displacement = map(op.sub, a, b)
    return sqrt(sum(d ** 2 for d in displacement))


def fixed_locations(drawing):
    # This is a brute-force n^2 algorithm. Could be improved
    points = filter(lambda e: e.dxftype() == 'POINT', drawing.modelspace())
    texts = list(filter(lambda e: e.dxftype() == 'TEXT', drawing.modelspace()))
    for point in points:
        location = point.get_dxf_attrib('location')
        closest = min(texts, key=lambda t: dist(location, t.get_dxf_attrib('insert')))

        try:
            height = float(closest.get_dxf_attrib('text'))
        except ValueError:
            continue

        yield location[:2] + (height,)


@click.command()
@click.argument('in_path', type=Path)
@click.argument('out_path', type=Path)
def main(in_path, out_path):
    fixed = fixed_locations(ezdxf.readfile(in_path))
    with r12writer(out_path) as dxf:
        for point in fixed:
            dxf.add_point(point)


if __name__ == "__main__":
    main()
