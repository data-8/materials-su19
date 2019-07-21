test = {
  'name': 'q2_1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(framingham_diabetes_possibilities) in [np.ndarray, list]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sorted(framingham_diabetes_possibilities) == [1,2,3]
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
