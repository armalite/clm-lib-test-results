# On-call notes - inventory-svc incident 2031-03-05

Informal running notes. Not reviewed; may be out of date.

- 08:03 flags/registry.json shows ff-pricing-async-v8 at 100% for inventory-svc and ff-ledger-encoder-v2 at 0% - if anything, suspect ff-pricing-async-v8.
- 08:55 front-proxy 500/503s for inventory-svc. db pool stats look normal.
- 09:06 No deploys of our service today per changes.log. Still investigating.
