test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cleaned_causes_by_year.sort("Year").select(sorted(cleaned_causes_by_year.labels)).take(range(5))
          All Other Causes | Alzheimer's Disease | Cerebrovascular Disease (Stroke) | Chronic Liver Disease and Cirrhosis | Chronic Lower Respiratory Disease (CLRD) | Diabetes Mellitus | Diseases of the Heart | Intentional Self Harm (Suicide) | Malignant Neoplasms (Cancers) | Pneumonia and Influenza | Unintentional Injuries | Year
          38,392           | 3,934               | 18,079                           | 3,546                               | 13,187                                   | 6,004             | 69,900                | 3,047                           | 52,880                        | 8,014                   | 8,940                  | 1,999
          39,259           | 4,398               | 18,090                           | 3,673                               | 12,754                                   | 6,203             | 68,533                | 3,113                           | 53,005                        | 8,355                   | 8,814                  | 2,000
          38,383           | 4,897               | 18,078                           | 3,759                               | 13,056                                   | 6,457             | 69,004                | 3,256                           | 53,810                        | 8,167                   | 9,274                  | 2,001
          41,177           | 5,405               | 17,551                           | 3,725                               | 12,643                                   | 6,783             | 68,387                | 3,210                           | 53,926                        | 8,098                   | 9,882                  | 2,002
          40,325           | 6,585               | 17,686                           | 3,832                               | 13,380                                   | 7,088             | 69,013                | 3,396                           | 54,307                        | 8,184                   | 10,470                 | 2,003
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
