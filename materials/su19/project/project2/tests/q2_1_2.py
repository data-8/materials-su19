test = {
  'name': 'q2_1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you can use any two movies;
          >>> correct_dis = 0.0011432060212606049;
          >>> dis = distance_two_features("titanic", "the avengers", "money", "feel");
          >>> np.isclose(dis, correct_dis)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you can use any two features;
          >>> correct_dis = 0.0041988885973385463;
          >>> dis = distance_two_features("titanic", "the avengers", "your", "that");
          >>> np.isclose(dis, correct_dis)
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
