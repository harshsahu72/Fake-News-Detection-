"""
model.py - Machine Learning Model (FakeNewsDetector)
Fake News Detector Project
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from config import Config, ConfidenceThresholds


class FakeNewsDetector:
    """
    Encapsulates the full ML pipeline:
      - TF-IDF feature extraction
      - Random Forest classification
      - Confidence / credibility scoring
    """

    def __init__(self, config: Config):
        """
        Initialise the detector with a Config instance.

        Args:
            config: Application configuration (model + vectorizer params).
        """
        vec_cfg = config.vectorizer
        model_cfg = config.model
        self._thresholds = config.thresholds

        self.vectorizer = TfidfVectorizer(
            max_features=vec_cfg.max_features,
            ngram_range=vec_cfg.ngram_range,
            stop_words=vec_cfg.stop_words,
            min_df=vec_cfg.min_df,
            max_df=vec_cfg.max_df,
        )

        self.classifier = RandomForestClassifier(
            n_estimators=model_cfg.n_estimators,
            max_depth=model_cfg.max_depth,
            min_samples_split=model_cfg.min_samples_split,
            min_samples_leaf=model_cfg.min_samples_leaf,
            random_state=model_cfg.random_state,
            class_weight=model_cfg.class_weight,
            n_jobs=-1,  # Use all CPU cores for speed
        )

        self.accuracy: float = 0.0
        self.n_estimators: int = model_cfg.n_estimators
        self.max_features: int = vec_cfg.max_features
        self._is_trained: bool = False

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def train(self, df) -> float:
        """
        Train the TF-IDF vectorizer and Random Forest on the provided dataset.

        Args:
            df: Pandas DataFrame with 'text' (str) and 'label' (0/1) columns.

        Returns:
            Accuracy score on the held-out test set.
        """
        if df is None or df.empty:
            raise ValueError("Training dataset is empty or None.")

        texts = df['text'].astype(str).tolist()
        labels = df['label'].tolist()

        # Vectorise
        X = self.vectorizer.fit_transform(texts)
        y = labels

        # Train / test split (80 / 20)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Fit classifier
        self.classifier.fit(X_train, y_train)

        # Evaluate
        y_pred = self.classifier.predict(X_test)
        self.accuracy = accuracy_score(y_test, y_pred)
        self._is_trained = True

        print(f"\n{'=' * 60}")
        print("MODEL TRAINING COMPLETE")
        print(f"{'=' * 60}")
        print(f"Accuracy: {self.accuracy * 100:.2f}%")
        print(f"Test samples: {len(y_test)}")
        print("\nDetailed Report:")
        print(classification_report(y_test, y_pred,
                                    target_names=['Real News', 'Fake News'],
                                    zero_division=0))
        print(f"{'=' * 60}")

        return self.accuracy

    # ------------------------------------------------------------------
    # Prediction
    # ------------------------------------------------------------------

    def predict(self, text: str) -> dict:
        """
        Predict whether the supplied text is real or fake news.

        Args:
            text: Pre-processed news article text.

        Returns:
            dict with keys:
              - is_fake (bool)
              - result (str) – human-readable verdict
              - confidence (str) – confidence percentage
              - credibility (str) – credibility level label
              - real_probability (str)
              - fake_probability (str)
              - word_count (int) – added by the route layer
        """
        if not self._is_trained:
            raise RuntimeError("Model has not been trained yet. Call train() first.")

        X = self.vectorizer.transform([text])
        prediction = int(self.classifier.predict(X)[0])
        probabilities = self.classifier.predict_proba(X)[0]

        # probabilities[0] = P(real), probabilities[1] = P(fake)
        real_prob = float(probabilities[0]) * 100
        fake_prob = float(probabilities[1]) * 100
        confidence = max(real_prob, fake_prob)

        is_fake = bool(prediction == 1)
        verdict = "LIKELY FAKE NEWS ⚠️" if is_fake else "LIKELY REAL NEWS ✅"
        credibility = self._get_credibility_label(confidence / 100)

        return {
            "is_fake": is_fake,
            "result": verdict,
            "confidence": f"{confidence:.1f}",
            "credibility": credibility,
            "real_probability": f"{real_prob:.1f}",
            "fake_probability": f"{fake_prob:.1f}",
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _get_credibility_label(self, confidence: float) -> str:
        """
        Map a 0-1 confidence value to a human-readable credibility string.

        Args:
            confidence: Float between 0 and 1.

        Returns:
            Credibility level string.
        """
        t = self._thresholds
        if confidence >= t.very_high:
            return "Very High Confidence"
        elif confidence >= t.high:
            return "High Confidence"
        elif confidence >= t.medium:
            return "Medium Confidence"
        else:
            return "Low Confidence"

    def get_stats(self) -> dict:
        """Return model performance statistics for the /api/stats endpoint."""
        return {
            "accuracy": f"{self.accuracy * 100:.2f}",
            "model_type": "Random Forest",
            "features": self.max_features,
            "n_estimators": self.n_estimators,
        }
