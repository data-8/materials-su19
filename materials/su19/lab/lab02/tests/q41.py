test = {
  'name': 'q41',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(really_highly_rated) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> really_highly_rated.num_rows == 29
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(really_highly_rated.sort(0).take([17]))
          Votes  | Rating | Title | Year | Decade
          895411 | 8.6    | Se7en | 1995 | 1990
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
