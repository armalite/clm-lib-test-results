# Incident board: updates in round 04

- Thread A status: mitigated (errors reduced after the applied change; monitoring).
- Thread B opened: errors in checkout-api. Suspected cause: an upstream provider rejecting requests with 429 (UPSTREAM_RATE_LIMIT). Status: ongoing.
- Thread D opened: a data volume running out of space alerts (DISK_PRESSURE) on search-api. Status: ongoing.
- Follow-up OPEN CUSTOMER_COMMS: customer communication about the impact.
- Follow-up OPEN POSTMORTEM_DRAFT: drafting the postmortem.
- Follow-up OPEN CAPACITY_REVIEW: capacity review of the affected tier.
