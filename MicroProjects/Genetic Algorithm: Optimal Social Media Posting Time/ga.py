import random
import math

# Precompute engagement scores for each hour with deterministic seed
random.seed(42)
HOURS = list(range(24))

def _true_engagement(h: int) -> float:
    """Simulated engagement score for a given hour."""
    return 50 + 40 * math.sin((h - 9) * math.pi / 12) + random.gauss(0, 5)

ENGAGEMENT_SCORES = [_true_engagement(h) for h in HOURS]


def fitness(hour: float) -> float:
    """Return negative engagement score; lower is better."""
    return -ENGAGEMENT_SCORES[int(hour) % 24]


def select(pop, scores, k: int = 3):
    """Tournament selection from the population."""
    selected = random.sample(range(len(pop)), k)
    best_idx = min(selected, key=lambda i: scores[i])
    return pop[best_idx]


def crossover(p1: float, p2: float) -> float:
    """Average the parents to create a child."""
    return (p1 + p2) / 2


def mutate(child: float, mutation_rate: float = 0.1) -> float:
    """Randomly mutate a child and keep result within 0-23."""
    if random.random() < mutation_rate:
        child += random.uniform(-1, 1)
    # ensure the hour stays within valid bounds
    return min(23, max(0, child))


def run_ga(n_gen: int = 50, pop_size: int = 30):
    """Run the genetic algorithm and return history, best hour and final population."""
    pop = [random.uniform(0, 23) for _ in range(pop_size)]
    history = []
    for _ in range(n_gen):
        scores = [fitness(x) for x in pop]
        best_idx = min(range(len(pop)), key=lambda i: scores[i])
        best = pop[best_idx]
        history.append(-scores[best_idx])
        new_pop = []
        for _ in range(pop_size):
            p1 = select(pop, scores)
            p2 = select(pop, scores)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)
        pop = new_pop
    return history, best, pop
