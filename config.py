"""
config.py - Centralized Configuration Management
Fake News Detector Project
"""

from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    """Random Forest model hyperparameters."""
    n_estimators: int = 200
    max_depth: int = 20
    min_samples_split: int = 5
    min_samples_leaf: int = 2
    random_state: int = 42
    class_weight: str = 'balanced'


@dataclass
class VectorizerConfig:
    """TF-IDF vectorizer settings."""
    max_features: int = 5000
    ngram_range: tuple = (1, 3)
    stop_words: str = 'english'
    min_df: int = 2
    max_df: float = 0.95


@dataclass
class ServerConfig:
    """Flask server configuration."""
    host: str = '0.0.0.0'
    port: int = 5000
    debug: bool = True


@dataclass
class ConfidenceThresholds:
    """Credibility confidence level thresholds."""
    very_high: float = 0.90
    high: float = 0.75
    medium: float = 0.60


@dataclass
class Config:
    """Master configuration aggregating all sub-configs."""
    model: ModelConfig = field(default_factory=ModelConfig)
    vectorizer: VectorizerConfig = field(default_factory=VectorizerConfig)
    server: ServerConfig = field(default_factory=ServerConfig)
    thresholds: ConfidenceThresholds = field(default_factory=ConfidenceThresholds)
    dataset_path: str = 'news.csv'
