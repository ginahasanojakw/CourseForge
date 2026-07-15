# === Stage 61: Add performance timing for core list and search operations ===
# Project: CourseForge
import time
from collections import Counter

class PerformanceTimer:
    def __init__(self):
        self.ops = {}

    def benchmark(self, name, func, *args, n=1000):
        """Run func(*args) repeatedly and report avg/median/max in ms."""
        times = []
        for _ in range(n):
            t0 = time.perf_counter_ns()
            result = func(*args)
            t1 = time.perf_counter_ns()
            times.append((t1 - t0) / 1e6)
        avg_ms, med_ms, max_ms = (
            sum(times)/len(times),
            sorted(times)[len(times)//2],
            max(times),
        )
        self.ops[name] = {
            'avg': avg_ms, 'median': med_ms, 'max': max_ms,
            'samples': n, 'result_sample': result if n == 1 else None,
        }
        return times[-1] / 1e3

    def report(self):
        """Print a compact summary table of all timed operations."""
        print(f"{'Op':<20} {'Avg(ms)':>9} {'Median(ms)':>11} {'Max(ms)':>8} {'Samples'}")
        for name, data in self.ops.items():
            print(
                f"{name:<20} {data['avg']:>9.3f} {data['median']:>11.3f} "
                f"{data['max']:>8.3f} {data['samples']}"
            )

if __name__ == '__main__':
    t = PerformanceTimer()

    # --- List operations ---
    def linear_search(lst, target):
        return next((i for i, x in enumerate(lst) if x == target), -1)

    def list_contains(lst, target):
        return target in lst

    def list_append_and_sum():
        acc = 0; s = []
        for _ in range(5000):
            s.append(_); acc += _
        return sum(s)

    # --- Search on dict / Counter ---
    def count_unique(lst):
        return len(set(lst))

    def counter_freq(lst, target):
        c = Counter(lst)
        return c[target]

    # --- Run benchmarks ---
    big_list = list(range(10_000))
    t.benchmark('linear_search', linear_search, big_list, 4242)
    t.benchmark('list_contains', list_contains, big_list, 9999)
    t.benchmark('append_and_sum', list_append_and_sum)
    t.benchmark('count_unique', count_unique, [1]*300 + [2]*700 + [3]*400 + [4]*600)
    t.benchmark('counter_freq', counter_freq, [1]*300 + [2]*700 + [3]*400 + [4]*600, 2)

    # --- Report ---
    t.report()
