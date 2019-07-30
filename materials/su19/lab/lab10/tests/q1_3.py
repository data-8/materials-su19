test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(sum(faithful_standard.column(0))) <= 1e-8
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(round(duration_std))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(round(wait_std))
          14
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
