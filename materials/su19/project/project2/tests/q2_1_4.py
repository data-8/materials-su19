test = {
  'name': 'q2_1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(close_movies.labels) >= {'Genre', 'Title', 'feel', 'money'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> close_movies.num_rows == 7
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
