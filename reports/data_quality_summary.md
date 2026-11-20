Day 1 – Data Quality Summary

1. Data Ingestion
- Source: MFAPI (https://api.mfapi.in/)
- Total schemes in fund master: 40
- Successfully fetched schemes: 34
- Unavailable schemes: 6
- Total NAV records: 99,975

2. Data Validation
- Missing values in NAV dataset: 0
- Duplicate NAV records: 0
- Successfully fetched scheme codes: 34
- Schemes without available NAV history: 6

3. Unavailable Scheme Codes
- 100016
- 100025
- 118635
- 102886
- 102887
- 148568

These API requests returned HTTP 200 but contained empty metadata and empty NAV data.


4 Monthly SIP Inflows - Data Quality Findings

Dataset: monthly_sip_inflows.csv

 Missing Values
- 12 missing values in yoy_growth_pct.
- All missing values belong to January-December 2022.
- These are potentially expected because prior-year comparison data is unavailable.

Potential Anomalies
- April 2025: new_sip_accounts_lakh = 46.0.
- January 2025: SIP AUM increased from 9.70 to 13.00 lakh crore.
- August 2025: SIP AUM increased from 14.05 to 15.18 lakh crore.

Recommendation
Investigate unusual values before performing further analysis.
Preserve the original raw dataset.


AMFI Scheme Code Analysis

- AMFI scheme codes uniquely identify mutual fund schemes.
- Regular and Direct plans have separate scheme codes.
- Scheme codes are used as common identifiers to connect fund_master and nav_history.
- Numeric digits should not be interpreted as fund-house or category identifiers without an official specification.

Validation Results
- Total unique codes in fund_master: 40
- Total unique codes in nav_history: 40
- Missing codes: 0
- Extra codes: 0
- Duplicate scheme-date records: 0

Conclusion: AMFI scheme-code validation passed.

Fund Master - Classification Findings

Dataset: `fund_master.csv`

- Total schemes: 40
- Missing category values: 0
- Blank category values: 0

Broad Category Distribution

| Category | Scheme Count | Percentage |
|---|---:|---:|
| Equity | 34 | 85% |
| Debt | 6 | 15% |
| **Total** | **40** | **100%** |

Risk Grade Distribution

| Risk Grade | Scheme Count |
|---|---:|
| Moderate | 16 |
| High | 8 |
| Very High | 6 |
| Low | 6 |
| Moderately High | 4 |
| **Total** | **40** |

 Observation

The `category` column contains broad classifications (Equity and Debt), while `sub_category` provides more specific classifications such as Mid Cap, Small Cap, Liquid and Gilt.

### Fund House Distribution

The dataset contains 40 mutual fund schemes from 10 fund houses.

| Fund House | Scheme Count |
|---|---:|
| SBI Mutual Fund | 5 |
| HDFC Mutual Fund | 5 |
| ICICI Prudential MF | 5 |
| Nippon India MF | 5 |
| Kotak Mahindra MF | 4 |
| Axis Mutual Fund | 4 |
| Aditya Birla Sun Life MF | 3 |
| UTI Mutual Fund | 3 |
| Mirae Asset MF | 3 |
| DSP Mutual Fund | 3 |
| **Total** | **40** |

**Observation:** SBI, HDFC, ICICI Prudential and Nippon India have the highest representation, with five schemes each.

5. Conclusion
NAV data was successfully ingested for 34 out of 40 mutual fund schemes. No missing values or duplicate records were identified in the fetched NAV dataset. Six scheme codes returned empty API responses and require further investigation.