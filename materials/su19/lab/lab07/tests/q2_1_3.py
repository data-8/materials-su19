test = {
  'name': 'q2_1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(diabetes_simulated_stats) == 5000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max(diabetes_simulated_stats) < .01
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.mean(diabetes_simulated_stats < .002) > .7
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
