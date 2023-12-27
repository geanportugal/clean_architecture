from flask import jsonify
import json
from flask import Blueprint, request, current_app
from framework.controllers.create_card_controller import (
    CreateCardController,
)


blueprint_create_card = Blueprint("create_card", __name__)


@blueprint_create_card.route("/card/", methods=["POST"])
def create_card_blueprint():
    """Create Card Blueprint"""
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = CreateCardController(logger)
    controller.get_card_info(input_json)
    result = controller.execute()

    return result, 201


@blueprint_create_card.route("/card/", methods=["GET"])
def get_card_blueprint():
    return jsonify({"hello": "word"})
