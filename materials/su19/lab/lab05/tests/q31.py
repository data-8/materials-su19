test = {
  'name': 'q31',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Warning: Charts will be displayed while running this test;
          >>> round(float(compute_statistics(full_data)[0]), 2) == 26.54
          True<Figure size 432x288 with 1 Axes><Figure size 432x288 with 1 Axes>
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Warning: Charts will be displayed while running this test;
          >>> round(float(compute_statistics(full_data)[1]), 2) == 4269775.77
          True<Figure size 432x288 with 1 Axes><Figure size 432x288 with 1 Axes>
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
