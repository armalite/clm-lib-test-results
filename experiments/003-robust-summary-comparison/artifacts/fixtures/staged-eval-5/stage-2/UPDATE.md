# Stage 2 of 3 (09:30-10:30 UTC)

On-call applied a mitigation (see stage-2/deploy/changes.log). The rates-svc timeouts stopped,
but ingress-a still returns 503s for quotes-api with a different error. New files below.
