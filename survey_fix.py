import ezdxf
from ezdxf.r12writer import R12FastStreamWriter
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
    with out_path.open("w") as f:
        # r12writer context manager doesn't seem to work if exception is thrown
        dxf = R12FastStreamWriter(f)
        try:
            for point in fixed:
                dxf.add_point(point)
        finally:
            dxf.close()


if __name__ == "__main__":
    main()
