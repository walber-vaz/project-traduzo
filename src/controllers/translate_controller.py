from deep_translator import GoogleTranslator
from flask import Blueprint, render_template, request

from models.history_model import HistoryModel
from models.language_model import LanguageModel

translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])  # type: ignore
def index():
    languages = LanguageModel.find()
    text_to_translate = "O que deseja traduzir"
    translated = "Tradução"
    translate_from = "pt"
    translate_to = "en"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translated_text = GoogleTranslator(
            source=translate_from, target=translate_to  # type: ignore
        ).translate(
            text_to_translate  # type: ignore
        )

        HistoryModel(
            {
                "text_to_translate": text_to_translate,
                "translated_text": translated_text,
                "translate_from": translate_from,
            }
        ).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text if request.method == "POST" else translated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translator = GoogleTranslator(source=translate_from, target=translate_to)
    translated_text = translator.translate(text_to_translate)

    translate_from, translate_to = translate_to, translate_from
    languages = LanguageModel.find()

    HistoryModel(
        {
            "text_to_translate": text_to_translate,
            "translated_text": translated_text,
            "translate_from": translate_from,
        }
    ).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text,
    )
