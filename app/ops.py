RUNBOOKS={
 "iam_denied":"capture principal, action, resource and CloudTrail evidence; do not broaden access blindly",
 "network_unreachable":"check route, security group, NACL, DNS and target health before changing firewall rules",
 "backup_failed":"preserve failure evidence and assess approved restore/retry path",
 "capacity_alarm":"confirm workload saturation and autoscaling limits before right-sizing"
}
def triage(event, evidence):
 if event not in RUNBOOKS: raise ValueError("unknown event")
 if not evidence: return {"status":"evidence_required","action":None}
 return {"status":"investigate","action":RUNBOOKS[event]}
