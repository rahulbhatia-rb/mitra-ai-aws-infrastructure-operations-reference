# AWS operations model

Start with scope, impact, timestamp and evidence. For connectivity, validate DNS, route tables, security groups/NACLs, NAT/VPN path and target health before making a change. For IAM, inspect the authenticated principal, explicit/implicit deny, resource policy and audit trail; use least privilege rather than broad role grants. Monitor availability, saturation, backup state, CloudTrail/control-plane events and security findings. A backup is only credible after tested restoration to the approved RTO/RPO.

Use reviewed Terraform/CloudFormation plans, controlled maintenance windows, a documented rollback and post-change validation. Escalate security, data-loss and cross-network boundary changes. Do not include credentials, customer data or infrastructure identifiers in tickets/logs beyond approved channels.
