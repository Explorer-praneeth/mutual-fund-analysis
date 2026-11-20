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

4. Conclusion
NAV data was successfully ingested for 34 out of 40 mutual fund schemes. No missing values or duplicate records were identified in the fetched NAV dataset. Six scheme codes returned empty API responses and require further investigation.