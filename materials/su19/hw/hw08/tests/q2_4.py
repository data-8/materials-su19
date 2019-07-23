test = {
  'name': 'q2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0<= min(HERS_test_statistics) <= 0.055
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(HERS_test_statistics) == 1000
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
