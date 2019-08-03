test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> not (abs(driving_start_time_hours - 5/3) > 4/9)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like your answer is in the ballpark, but;
          >>> # not quite right.  Hint: Try finding a place where;
          >>> # the line intersects a crossing of two grid lines.;
          >>> not (1/9 < abs(driving_start_time_hours - 5/3) < 4/9)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 14/9 <= driving_start_time_hours <= 16/9
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
