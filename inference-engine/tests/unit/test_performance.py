import unittest
import time
from src.utils.performance_tracker import PerformanceTracker

class TestPerformanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = PerformanceTracker()

    def test_performance_tracking(self):
        self.tracker.start_tracking()
        time.sleep(0.1)  # Simulate some work
        metrics = self.tracker.stop_tracking(step_count=5)
        
        self.assertGreater(metrics.execution_time, 0)
        self.assertGreater(metrics.memory_usage, 0)
        self.assertGreaterEqual(metrics.cpu_usage, 0)
        self.assertEqual(metrics.step_count, 5)

    def test_performance_report(self):
        self.tracker.start_tracking()
        time.sleep(0.1)  # Simulate some work
        self.tracker.stop_tracking(step_count=5)
        
        report = self.tracker.get_performance_report()
        self.assertIn("execution_time_ms", report)
        self.assertIn("memory_usage_mb", report)
        self.assertIn("cpu_usage_percent", report)
        self.assertIn("steps_processed", report)

if __name__ == '__main__':
    unittest.main()