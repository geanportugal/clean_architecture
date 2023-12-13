from flask import jsonify
from flask import Blueprint, request, current_app
from src.framework.flask.controllers.create_card_controller import CreateCardController


blueprint_create_card = Blueprint("create_card", __name__)


@blueprint_create_card.route("/api/V1/card/", methods=["POST"])
def create_card_blueprint():
    """Create Card Blueprint"""
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = CreateCardController(logger)
    controller.get_card_info(input_json)
    result = controller.execute()
    return jsonify(result), 201
