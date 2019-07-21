test = {
  'name': 'q2_2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(framingham_observed_statistic, (float, int, np.integer))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> abs(framingham_observed_statistic - compute_framingham_test_statistic(framingham)) < 1e-6
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
