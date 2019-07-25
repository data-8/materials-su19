test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.random.seed(49);
          >>> _sim_test_stat = simulate_one_HERS_statistic();
          >>> np.isclose(_sim_test_stat, 0.014203527303593325) or np.isclose(_sim_test_stat, 0.006965009902857672)
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
