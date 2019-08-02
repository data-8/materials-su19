test = {
  'name': 'q1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(regression_changes) == 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure regression_changes is an array;
          >>> type(regression_changes)
          numpy.ndarray
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
