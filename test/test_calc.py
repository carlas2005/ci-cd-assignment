# test/test_pt_calc.py
import pytest
from datetime import datetime, timedelta
from src.pt_calc import get_time

def test_missing_points_calculated_correctly():
    hours, minutes, _ = get_time(actual_pts=3, needed_pts=10, time_for_pt=30)
    # 7 pts missing × 30 min = 210 min = 3h 30min
    assert hours == 3
    assert minutes == 30

def test_no_missing_points_returns_zero():
    hours, minutes, _ = get_time(actual_pts=10, needed_pts=10, time_for_pt=30)
    assert hours == 0
    assert minutes == 0

def test_more_points_than_needed_returns_zero():
    hours, minutes, _ = get_time(actual_pts=15, needed_pts=10, time_for_pt=30)
    assert hours == 0
    assert minutes == 0

def test_exact_one_hour_wait():
    hours, minutes, _ = get_time(actual_pts=0, needed_pts=2, time_for_pt=30)
    assert hours == 1
    assert minutes == 0

def test_only_minutes():
    hours, minutes, _ = get_time(actual_pts=9, needed_pts=10, time_for_pt=45)
    assert hours == 0
    assert minutes == 45

def test_time_charged_is_correct():
    actual_pts = 0
    needed_pts = 5
    time_for_pt = 30  

    _, _, time_charged = get_time(actual_pts, needed_pts, time_for_pt)

    expected_delta = timedelta(minutes=(needed_pts - actual_pts) * time_for_pt)
    now = datetime.now()

    # Compare time difference between time_charged and now
    diff = abs((time_charged - now) - expected_delta)
    
    assert diff < timedelta(seconds=1)