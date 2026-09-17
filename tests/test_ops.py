import unittest
from app.ops import triage
from app.change import change_ready
class Operations(unittest.TestCase):
 def test_identity_needs_evidence(self): self.assertEqual(triage("iam_denied",{})["status"],"evidence_required")
 def test_network_is_ordered(self): self.assertIn("route",triage("network_unreachable",{"ticket":"x"})["action"])
 def test_change_requires_rollback(self):
  self.assertFalse(change_ready({"owner":"r","window":"x","validation":"x"}))
  self.assertTrue(change_ready({"owner":"r","window":"x","validation":"x","rollback":"x"}))
