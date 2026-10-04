S1: rel-notes 7.20.4-0a00 line8 rates timeout 2500->600; line16 db pool 48->12. quotes-api.log first timeout line139 (600ms). deploys.log:4 deploy 08:16.
db pool wait in_use 12/12 at quotes-api.log:150,177,219,357 (few WARN only).
ingress 503 first at ingress-a.log:71; 60 503s total
advanced to stage2
