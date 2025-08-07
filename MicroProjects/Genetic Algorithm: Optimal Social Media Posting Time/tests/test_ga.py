import importlib.util
import pathlib
import random

# Load the GA module from the same directory
MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "ga.py"
spec = importlib.util.spec_from_file_location("ga", MODULE_PATH)
ga = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ga)


def test_mutate_keeps_within_bounds():
    random.seed(0)
    for _ in range(100):
        mutated = ga.mutate(22, mutation_rate=1.0)
        assert 0 <= mutated <= 23


def test_run_ga_best_hour_and_population_size():
    random.seed(0)
    history, best_hour, pop = ga.run_ga(n_gen=10, pop_size=15)
    optimal_hour = ga.ENGAGEMENT_SCORES.index(max(ga.ENGAGEMENT_SCORES))
    assert int(round(best_hour)) == optimal_hour
    assert len(pop) == 15
