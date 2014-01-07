from flask import Flask, request, make_response
import json
app = Flask(__name__)

shopping_list = []

@app.route("/shopping_list", methods=['GET', 'POST', 'DELETE'])
def shopping_list_route():

	if request.method == "GET":
		if "Accept" in request.headers and request.headers["Accept"] == "application/json":
			response = make_response("[" + ", ".join(shopping_list) + "]", 200)
			response.headers["Content-Type"] = "application/json"
			return response

	elif request.method == "POST":			

		json = request.get_json()
		if json:
			if "shopping_list_item" in json:
				shopping_list.append(json["shopping_list_item"])
		
				return make_response("/shopping_list/{0}".format(len(shopping_list) -1), 200)
			else:
				return make_response("Item aint there", 400)
		else:
			return make_response("Bad request asd", 400)
	
	elif request.method == "DELETE":
		del shopping_list[:]
		return make_response("", 204)


@app.route("/shopping_list/<int:index>", methods=['GET', 'DELETE'])
def shopping_list_item(index):
	if index >= 0 and index < len(shopping_list):
		if request.method == "GET":
			response =  make_response(json.dumps(shopping_list[index]), 200)
			response.headers["Content-Type"] = "application/json"
			return response

		elif request.method == "DELETE":
			del shopping_list[index]
			return make_response("", 204)

	else:
		return make_response("Index out of range", 404)
	

def main():
	app.run(debug=True)	

if __name__ == '__main__':
	main()
