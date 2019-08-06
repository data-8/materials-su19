test = {
  'name': 'q3_3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_movie_correctness.labels == ('Title', 'Genre', 'Was correct')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test_movie_correctness.num_rows == test_movies.num_rows
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(test_movie_correctness.group('Genre'))
          Genre   | count
          action  | 21
          romance | 16
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
