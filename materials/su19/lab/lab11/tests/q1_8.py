test = {
  'name': 'q1_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(best_line_slope, 1)
          14094.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(best_line_intercept, 1)
          2.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(new_errors) == 156
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(new_errors[10], 1)
          -12.3
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
