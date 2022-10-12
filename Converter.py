from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
node_list = []
start_flag = False


def speed_to_c(option, option_name):
    match option_name:
        case "meter_per_second":
            return option
        case "kilometer_per_hour":
            return option * (5 / 18)
        case "mile_per_hour":
            return option * 0.477
        case "foot_per_second":
            return option * 0.3048


def temp_to_c(option, option_name):
    match option_name:
        case "kelvin":
            return option + 273
        case "celsius":
            return option
        case "fahrenheit":
            return ((option - 32) * 5) / 9
        case "reaumur":
            return option * 1.25


def length_to_c(option, option_name):
    match option_name:
        case "kilometer":
            return option * 1000
        case "meter":
            return option
        case "centimeter":
            return option / 100
        case "mile":
            return option * 1609
        case "foot":
            return option / 3.281
        case "inch":
            return option / 39.37
        case "versta":
            return option * 1066
        case "sazhen":
            return option * 2.1336
        case "arshin":
            return option * 0.7112


def weight_to_c(option, option_name):
    match option_name:
        case "kilogram":
            return option * 1000
        case "gram":
            return option
        case "milligram":
            return option / 1000
        case "stone":
            return option * 6350
        case "pound":
            return option * 453.6
        case "ounce":
            return option * 28.35
        case "pud":
            return option * 16380
        case "grivna":
            return option * 51
        case "lot":
            return option * 12.7


def convert_to_c(option, option_type, option_name):
    match option_type:
        case "weight":
            return weight_to_c(option, option_name)
        case "length":
            return length_to_c(option, option_name)
        case "temperature":
            return temp_to_c(option, option_name)
        case "speed":
            return speed_to_c(option, option_name)


def c_to_weight(option, option_name):
    match option_name:
        case "kilogram":
            return option / 1000
        case "gram":
            return option
        case "milligram":
            return option * 1000
        case "stone":
            return option / 6350
        case "pound":
            return option / 453.6
        case "ounce":
            return option / 28.35
        case "pud":
            return option / 16380
        case "grivna":
            return option / 51
        case "lot":
            return option / 12.7


def c_to_length(option, option_name):
    match option_name:
        case "kilometer":
            return option / 1000
        case "meter":
            return option
        case "centimeter":
            return option * 100
        case "mile":
            return option / 1609
        case "foot":
            return option * 3.281
        case "inch":
            return option * 39.37
        case "versta":
            return option / 1066
        case "sazhen":
            return option / 2.1336
        case "arshin":
            return option / 0.7112


def c_to_temp(option, option_name):
    match option_name:
        case "kelvin":
            return option - 273
        case "celsius":
            return option
        case "fahrenheit":
            return (option * (9 / 5)) + 32
        case "reaumur":
            return option / 1.25


def c_to_speed(option, option_name):
    match option_name:
        case "meter_per_second":
            return option
        case "kilometer_per_hour":
            return option / (5 / 18)
        case "mile_per_hour":
            return option / 0.477
        case "foot_per_second":
            return option / 0.3048


def convert_from_c(option, option_type, option_name):
    match option_type:
        case "weight":
            return c_to_weight(option, option_name)
        case "length":
            return c_to_length(option, option_name)
        case "temperature":
            return c_to_temp(option, option_name)
        case "speed":
            return c_to_speed(option, option_name)


@app.route("/convert/<int:option>/<string:option_type>/<string:option_name_1>/<string:option_name_2>", methods=['GET'])
@cross_origin()
def convert(option, option_type, option_name_1, option_name_2):
    option_c = convert_to_c(option, option_type, option_name_1)
    c_option = convert_from_c(option_c, option_type, option_name_2)
    print(c_option)
    if c_option is None:
        return jsonify("400 Bad Request You Are Sick With LIGMA")
    return jsonify(c_option)

if __name__ == '__main__':
    from waitress import serve

    print("launching")
    print("starting server")
    serve(app, port=5000)
    # app.run(debug=True)
