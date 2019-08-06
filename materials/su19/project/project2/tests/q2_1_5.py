test = {
  'name': 'q2_1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [most_common('Genre', close_movies.take(range(k))) for k in range(1, 8, 2)]
          ['romance', 'romance', 'romance', 'romance']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> [most_common('Genre', close_movies.take(range(7-k, 7))) for k in range(1, 8, 2)]
          ['romance', 'romance', 'romance', 'romance']
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
