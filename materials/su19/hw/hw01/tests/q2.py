test = {
  'name': 'Question 2_',
  'points': 1,
  'suites': [
        {
          'cases': [
            {
              'code': r"""
              >>> 1 <= characters_q1 <= 5
              True
              >>> 1 <= characters_q2 <= 3
              True
              """,
              'hidden': False,
              'locked': False
            },
            {
              'code': r"""
              >>> characters_q1 == 2
              True
              >>> characters_q2 == 1
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
