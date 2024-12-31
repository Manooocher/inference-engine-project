import time
from typing import Dict, List, Optional, Callable
import psutil
import os
from dataclasses import dataclass
from functools import wraps

@dataclass
class PerformanceMetrics:
    execution_time: float
    memory_usage: float
    cpu_usage: float
    step_count: int

class PerformanceTracker:
    def __init__(self):
        self.start_time: float = 0
        self.end_time: float = 0
        self.metrics: List[PerformanceMetrics] = []

    def start_tracking(self) -> None:
        """
        Starts tracking performance metrics
        """
        self.start_time = time.time()

    def stop_tracking(self, step_count: int) -> PerformanceMetrics:
        """
        Stops tracking and records final metrics
        """
        self.end_time = time.time()
        metrics = PerformanceMetrics(
            execution_time=self.end_time - self.start_time,
            memory_usage=psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
            cpu_usage=psutil.Process(os.getpid()).cpu_percent(),
            step_count=step_count
        )
        self.metrics.append(metrics)
        return metrics

    def get_performance_report(self) -> Dict:
        """
        Generates a detailed performance report
        """
        if not self.metrics:
            return {"error": "No performance data available"}

        latest_metrics = self.metrics[-1]
        return {
            "execution_time_ms": round(latest_metrics.execution_time * 1000, 2),
            "memory_usage_mb": round(latest_metrics.memory_usage, 2),
            "cpu_usage_percent": round(latest_metrics.cpu_usage, 2),
            "steps_processed": latest_metrics.step_count,
            "average_time_per_step_ms": round(
                (latest_metrics.execution_time * 1000) / latest_metrics.step_count
                if latest_metrics.step_count > 0 else 0,
                2
            )
        }

    @staticmethod
    def track_performance(func: Callable) -> Callable:
        """
        Decorator for tracking performance of individual functions
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            performance_data = {
                "function_name": func.__name__,
                "execution_time_ms": round(execution_time * 1000, 2),
                "memory_usage_mb": round(
                    psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024,
                    2
                )
            }
            
            if hasattr(result, "performance_data"):
                result.performance_data = performance_data
            
            return result
        
        return wrapper
