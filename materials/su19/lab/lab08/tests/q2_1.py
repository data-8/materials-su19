test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # This is a little magic to make sure that you see the same results;
          >>> # we did.;
          >>> np.random.seed(123);
          >>> 
          >>> one_resample = simulate_resample();
          >>> ten_rows = one_resample.take(np.arange(10));
          >>> ten_rows
          serial number
          108
          57
          57
          36
          41
          42
          47
          50
          135
          47
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.random.seed(123);
          >>> 
          >>> one_resample = simulate_resample();
          >>> one_resample.num_rows == 17
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
