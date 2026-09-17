# AWS Infrastructure Operations Reference — Mitra AI application

A testable control model for AWS cloud operations: asset health triage, IAM/network evidence, backup/recovery decisions and change safety. Prepared by Rahul H Bhatia for Mitra AI’s AWS Cloud & Infrastructure Engineer remote contract. This is a portfolio project, not a Mitra AI environment or deployed infrastructure.

## Evidence

- `app/ops.py`: classifies AWS operational events and requires evidence before an action is recommended.
- `app/change.py`: gates change requests on owner, rollback and validation fields.
- `tests/test_ops.py`: covers identity, network, backup and change-control paths.
- `docs/aws-operations.md`: practical VPC/IAM, monitoring, recovery and security workflow.

```bash
python -m unittest discover -s tests -v
```

The post requests Windows/Linux, AD/DNS/DHCP, VPN/Direct Connect and many monitoring/security products. This artifact represents AWS/Terraform/CloudFormation, network/IAM and production-operations approach; it does not claim hands-on production depth in every named Windows/AD or commercial tool.

## Contact

Rahul H Bhatia  
[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
