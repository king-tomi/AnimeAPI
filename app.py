from flask import Flask, jsonify
from flask_restful import Api, Resource
from scraper import Scraper

app = Flask(__name__)
api = Api(app)

PARTS = (
    "anime",
    "manga"
)

class GetResource(Resource):

    def get(self, section: str, name: str, target: str):
        if section not in PARTS:
            return "request does not exists", 401

        if section == "anime":
            if target == "reviews":
                sent = "/" + section + "/" + name + "/" + target
                scraper = Scraper(sent)
                value = scraper.sieve_anime_reviews()
                return jsonify({"reviews": value})
            elif target == "ratings":
                sent = "/" + section + "/" + name + "/" + target
                scraper = Scraper(sent)
                value = scraper.sieve_anime_ratings()
                return jsonify({"ratings": value})
            elif target == "characters":
                sent = "/" + section + "/" + name + "/" + target
                scraper = Scraper(sent)
                value = scraper.sieve_characters()
                return jsonify({"characters": value})
            else:
                return jsonify({"value": None})

        elif section == "manga":
            if target == "reviews":
                sent = "/" + section + "/" + name + "/" + target
                scraper = Scraper(sent)
                value = scraper.sieve_manga_reviews()
                return jsonify({"reviews": value})
            elif target == "ratings":
                sent = "/" + section + "/" + name + "/" + target
                scraper = Scraper(sent)
                value = scraper.sieve_manga_ratings()
                return jsonify({"ratings": value})
            elif target == "characters":
                sent = "/" + section + "/" + name + "/" + target
                scraper = Scraper(sent)
                value = scraper.sieve_characters()
                return jsonify({"characters": value})
            else:
                return jsonify({"value": None})

        else:
            return jsonify({"value": None})


class GetInfo(Resource):

    def get(self, section: str, name: str):
        sent = "/" + section + "/" + name
        scraper = Scraper(sent)
        value = scraper.sieve_info()
        return jsonify({"info": value})


api.add_resource(GetResource, "/api/<string:section>/<string:name>/<string:target>")

api.add_resource(GetInfo, "/api/<string:section>/<string:name>")