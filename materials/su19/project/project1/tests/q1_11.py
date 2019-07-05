test = {
  'name': 'q1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Incorrect labels for columns;
          >>> t = stats_for_year(1990);
          >>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Incorrect number of rows;
          >>> t = stats_for_year(1990);
          >>> t.num_rows
          50
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))
          geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
          chn  | 644,450,173      | 3.99                               | 309
          egy  | 27,072,397       | 6.63                               | 312.8
          gha  | 6,652,285        | 6.75                               | 210.9
          ita  | 49,714,962       | 2.37                               | 52
          mex  | 38,174,114       | 6.78                               | 142.9
          npl  | 10,056,945       | 5.99                               | 327.1
          prk  | 11,424,179       | 4.58                               | 127.3
          tur  | 27,553,280       | 6.3                                | 249
          uzb  | 8,789,492        | 6.71                               | 175.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))
          geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
          bra  | 198,614,208      | 1.84                               | 16.7
          deu  | 80,435,307       | 1.39                               | 4.2
          fra  | 62,961,136       | 1.98                               | 4.3
          irn  | 74,253,373       | 1.9                                | 19.2
          kor  | 49,090,041       | 1.27                               | 4.1
          mys  | 28,119,500       | 2                                  | 8.3
          phl  | 93,038,902       | 3.15                               | 31.9
          sdn  | 36,114,885       | 4.64                               | 80.2
          ukr  | 45,647,497       | 1.44                               | 11.8
          yem  | 23,591,972       | 4.5                                | 58.8
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
