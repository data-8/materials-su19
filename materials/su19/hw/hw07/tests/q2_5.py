test = {
  'name': 'q2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(interpretations) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(interpretations) > 0
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
