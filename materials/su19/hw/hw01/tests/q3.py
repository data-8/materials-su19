test = {
  'name': 'Question 3_',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 1 <= names_q1 <= 4
          True
          >>> 1 <= names_q2 <= 4
          True
          >>> 1 <= names_q3 <= 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> names_q1 == 2
          True
          >>> names_q2 == 4
          True
          >>> names_q3 == 2
          True
          """,
          'hidden': True,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
