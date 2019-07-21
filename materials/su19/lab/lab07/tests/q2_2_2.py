test = {
  'name': 'q2_2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(compute_framingham_test_statistic(framingham), (float, int, np.integer))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fake_framingham1 = Table().with_columns('TOTCHOL', make_array(200, 225, 250, 275), 'ANYCHD', make_array(1, 0, 0, 1));
          >>> fake_framingham2 = Table().with_columns('TOTCHOL', make_array(200, 225, 250, 275), 'ANYCHD', make_array(0, 0, 1, 1));
          >>> compute_framingham_test_statistic(fake_framingham1) < compute_framingham_test_statistic(fake_framingham2)
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
