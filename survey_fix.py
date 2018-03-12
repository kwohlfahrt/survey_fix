import ezdxf
from ezdxf.r12writer import r12writer
import click
from pathlib import Path
import operator as op
from math import sqrt
from functools import partial


def dist(a, b):
    displacement = map(op.sub, a, b)
    return sqrt(sum(d ** 2 for d in displacement))


def marker_location(element):
    dxftype = element.dxftype()
    if dxftype == "POINT":
        return element.get_dxf_attrib('location')
    else:
        raise ValueError("Unrecognized element type: {}".format(dxftype))


def fixed_locations(drawing):
    # This is a brute-force n^2 algorithm. Could be improved
    heights = {}
    for text in drawing.modelspace().query("TEXT"):
        location = text.get_dxf_attrib('insert')
        try:
            height = float(text.get_dxf_attrib('text'))
        except ValueError:
            heights[location] = None
        else:
            heights[location] = height

    markers = drawing.modelspace().query("POINT")
    for location in map(marker_location, markers):
        closest = min(heights, key=partial(dist, location))
        height = heights[closest]
        if height is not None:
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
