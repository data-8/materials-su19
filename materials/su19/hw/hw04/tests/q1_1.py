test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "Cause of Death" in cleaned_causes.labels
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you forgot to do the third step ;
          >>> # in dropping the abbreviations and renaming the description;
          >>> "Cause of Death (Full Description)" not in cleaned_causes.labels
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(np.unique(cleaned_causes.group('Cause of Death').column(1)))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(np.unique(cleaned_causes.group('Cause of Death').column(1).item(0)))
          22868
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
