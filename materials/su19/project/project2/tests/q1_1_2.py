test = {
  'name': 'q1_1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> unstemmed_run.item(0).startswith('run')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(unstemmed_run) > 1
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
