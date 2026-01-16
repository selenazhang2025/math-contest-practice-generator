from mcpgen.core import GeneratorConfig, generate_set


def test_reproducible_with_seed():
    cfg1 = GeneratorConfig(n=5, difficulty=3, topics=None, seed=123)
    cfg2 = GeneratorConfig(n=5, difficulty=3, topics=None, seed=123)
    s1 = generate_set(cfg1)
    s2 = generate_set(cfg2)
    assert [p.prompt for p in s1.problems] == [p.prompt for p in s2.problems]
    assert [p.answer for p in s1.problems] == [p.answer for p in s2.problems]


def test_topic_filtering():
    cfg = GeneratorConfig(n=10, difficulty=2, topics=["algebra"], seed=1)
    s = generate_set(cfg)
    assert all(p.topic == "algebra" for p in s.problems)
