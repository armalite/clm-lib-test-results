# Stage 2 of 3 (09:30-10:30 UTC)

On-call applied a mitigation (see stage-2/deploy/changes.log). The pricing-core timeouts stopped,
but front-proxy still returns 503s for billing-svc with a different error. New files below.
