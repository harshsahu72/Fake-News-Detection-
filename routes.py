"""
routes.py - Flask API Route Definitions
Fake News Detector Project
"""

from flask import request, jsonify, render_template_string
from templates import get_html_template


def register_routes(app, model, text_processor):
    """
    Register all HTTP routes on the Flask application.

    Args:
        app: Flask application instance.
        model: Trained FakeNewsDetector instance.
        text_processor: TextProcessor instance.
    """

    # ------------------------------------------------------------------
    # Home Page
    # ------------------------------------------------------------------

    @app.route('/', methods=['GET'])
    def index():
        """Serve the main HTML interface."""
        return render_template_string(get_html_template())

    # ------------------------------------------------------------------
    # POST /api/analyze
    # ------------------------------------------------------------------

    @app.route('/api/analyze', methods=['POST'])
    def analyze():
        """
        Analyze a news article for fake news detection.

        Request JSON:
            { "text": "<article text>" }

        Response JSON:
            { "success": true, "result": { ... } }
            OR
            { "success": false, "error": "<message>" }
        """
        try:
            data = request.get_json(silent=True)

            if not data:
                return jsonify({
                    "success": False,
                    "error": "Request body must be valid JSON."
                }), 400

            raw_text = data.get('text', '').strip()

            if not raw_text:
                return jsonify({
                    "success": False,
                    "error": "No text provided."
                }), 400

            # Validate before expensive preprocessing
            if not text_processor.validate_text(raw_text, min_words=3):
                return jsonify({
                    "success": False,
                    "error": "Text is too short or invalid. Please provide at least 3 words."
                }), 400

            # Preprocess
            cleaned_text = text_processor.preprocess_text(raw_text)

            # Predict
            result = model.predict(cleaned_text)

            # Enrich with word count (from original text to reflect UI count)
            result['word_count'] = text_processor.get_word_count(raw_text)

            return jsonify({"success": True, "result": result})

        except ValueError as exc:
            return jsonify({"success": False, "error": str(exc)}), 400
        except RuntimeError as exc:
            return jsonify({"success": False, "error": str(exc)}), 503
        except Exception as exc:  # pylint: disable=broad-except
            return jsonify({"success": False, "error": f"Internal server error: {str(exc)}"}), 500

    # ------------------------------------------------------------------
    # GET /api/stats
    # ------------------------------------------------------------------

    @app.route('/api/stats', methods=['GET'])
    def stats():
        """
        Return model performance statistics.

        Response JSON:
            { "accuracy": "92.50", "model_type": "...", "features": 5000, ... }
        """
        try:
            return jsonify(model.get_stats())
        except Exception as exc:  # pylint: disable=broad-except
            return jsonify({"error": str(exc)}), 500
