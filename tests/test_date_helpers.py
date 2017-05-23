from datetime import datetime
from itertools import starmap

from basic_utils.date_helpers import date_ranges_overlap, dates_between


def test_dates_between() -> None:
    start = datetime(2016, 1, 1)
    end = datetime(2016, 1, 3)
    expected = starmap(datetime, ((2016, 1, 1), (2016, 1, 2), (2016, 1, 3)))
    assert tuple(dates_between(start, end)) == tuple(expected)


def test_ranges_overlap() -> None:
    rangeX = (datetime(2012, 1, 15), datetime(2012, 5, 10))
    rangeY = (datetime(2012, 3, 20), datetime(2012, 9, 15))
    assert date_ranges_overlap(rangeX, rangeY)

    rangeX = (datetime(2012, 1, 15), datetime(2012, 5, 10))
    rangeY = (datetime(2015, 3, 20), datetime(2015, 9, 15))
    assert not date_ranges_overlap(rangeX, rangeY)
