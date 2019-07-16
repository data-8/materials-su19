test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> origin_landing = landing_distance(0, 0);
          >>> origin_landing == 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> positives_landing = landing_distance(50, 25);
          >>> 54 < positives_landing < 56
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
