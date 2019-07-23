test = {
  'name': 'q3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> left_end_1 == percentile(2.5, bootstrap_mean_based_estimates)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> right_end_1 == percentile(97.5, bootstrap_mean_based_estimates)
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
