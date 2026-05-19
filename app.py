"""
app.py - Application Entry Point
Fake News Detector Project
"""

from flask import Flask
from config import Config
from data_loader import DataLoader
from text_processor import TextProcessor
from model import FakeNewsDetector
from routes import register_routes


def create_app() -> tuple:
    """
    Initialize and return the Flask app plus trained detector.

    Returns:
        (Flask app, FakeNewsDetector) tuple.
    """
    print("=" * 60)
    print("FAKE NEWS DETECTOR - MACHINE LEARNING PROJECT")
    print("=" * 60)

    # 1. Load configuration
    config = Config()

    # 2. Initialize components
    data_loader = DataLoader()
    text_processor = TextProcessor()

    # 3. Load dataset
    print("\nLoading dataset...")
    df = data_loader.load_dataset(config.dataset_path)

    # 4. Train model
    print("\nTraining Random Forest model...")
    model = FakeNewsDetector(config)
    model.train(df)

    # 5. Bootstrap Flask app
    app = Flask(__name__)

    # 6. Register routes
    register_routes(app, model, text_processor)

    return app, model


def main():
    app, _ = create_app()

    print(f"\nStarting Flask server...")
    print(f"Open your browser and go to: http://127.0.0.1:5000")
    print("=" * 60)

    from config import Config
    cfg = Config()
    app.run(
        host=cfg.server.host,
        port=cfg.server.port,
        debug=cfg.server.debug,
    )


if __name__ == '__main__':
    main()
