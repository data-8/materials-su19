test = {
  'name': 'Question 7_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(survivor_answer) == int
          True
          >>> 1 <= survivor_answer <= 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> survivor_answer == 1
          True
          """,
          'hidden': True,
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
