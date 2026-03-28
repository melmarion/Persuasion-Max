# Validation Results

## Summary

| Metric | Value |
|--------|-------|
| Circuit classification accuracy | 56.0% (28/50) |
| Weak dimension accuracy | 26.0% (13/50) |
| Compliance-conversion correlation (r) | 0.389 |
| Effectiveness-conversion correlation (r) | 0.474 |
| Mean effectiveness (high-converting) | 77.9% |
| Mean effectiveness (low-converting) | 67.4% |
| Separation | +10.5 pp |
| 7D model accuracy | 56.0% |
| 2D (valence-arousal) accuracy | 46.0% |
| 7D advantage | +10.0 pp |
| TRIBE v2 alignment (r) | 0.776 |

## Confusion Matrix

| True \ Predicted | approach | avoidance | deliberation |
|------------------|----------|-----------|--------------|
| approach | 24 | 1 | 0 |
| avoidance | 8 | 4 | 0 |
| deliberation | 12 | 1 | 0 |

## Ablation Study

| Dimension | Accuracy Without | Degradation | Importance Rank |
|-----------|-----------------|-------------|-----------------|
| valence | 50.0% | 6.0 pp | #1 |
| novelty | 56.0% | 0.0 pp | #2 |
| coping_potential | 56.0% | 0.0 pp | #3 |
| agency | 56.0% | 0.0 pp | #4 |
| certainty | 56.0% | 0.0 pp | #5 |
| temporal_proximity | 56.0% | 0.0 pp | #6 |
| goal_relevance | 58.0% | -2.0 pp | #7 |

## 7-Dimension vs 2-Dimension Benchmark

7-dimension appraisal model outperforms 2-dimension valence-arousal by 10.0 percentage points (56.0% vs 46.0%), demonstrating that cognitive appraisal theory adds predictive value beyond simple sentiment analysis.