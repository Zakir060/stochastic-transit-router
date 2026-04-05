# NYC TLC Dataset

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document describes trip record ingestion from the official NYC TLC portal and the outlier policy used for travel-time estimation.

## Parquet schema fields

| Column name | Type | Description | Used for | Outlier threshold |
|:--|:--|:--|:--|:--|
| pickup_datetime | timestamp | trip start time | duration and segmentation | none |
| dropoff_datetime | timestamp | trip end time | duration and segmentation | none |
| trip_distance | float | reported distance in miles | speed and quality checks | 0.1 to 200 |
| PULocationID | int | pickup zone | zone pair mapping | positive ID |
| DOLocationID | int | dropoff zone | zone pair mapping | positive ID |
| total_amount | float | paid amount | descriptive analytics | non negative |
| congestion_surcharge | float | congestion fee | context feature | non negative |

## Outlier policy

| Field | Lower bound | Upper bound | Action | Logged |
|:--|:--|:--|:--|:--|
| trip_duration_seconds | 60 | 10800 | remove row | yes |
| speed_mph | 0.1 | 80 | remove row | yes |
| trip_distance | 0.1 | 200 | remove row | yes |
| total_amount | 0 | 2000 | remove row | yes |

## Speed formula

$$
speed_mph = \\frac{trip_distance_miles}{trip_duration_seconds / 3600}
$$

## Related

- [TLC trip cleaning](/src/tlc/cleaner.py)
- [TLC feature extraction](/src/tlc/feature_extractor.py)
- [Estimation](/docs/math/estimation.md)

---

Document Control

- Owner: Data Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
