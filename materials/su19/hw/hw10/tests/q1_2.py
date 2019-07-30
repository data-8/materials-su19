test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(resampled_means) == type(make_array())
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(resampled_means) == 5000
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
