from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def base_page():
	
	request.args
	
	print(request.args)
	
	page_string = ''
	
	if 'noun' not in request.args.keys():
		page_string += '<form>'
		page_string += 'Noun: <input name="noun"><br/>'
		page_string += 'Verb: <input name="verb"><br/>'
		page_string += 'adj: <input name="adj"><br/>'
		page_string += '<input type="submit">'
		page_string += '</form>'
	else:
		noun = request.args['noun']
		verb = request.args['verb']
		adj = request.args['adj']
		
		page_string += f'A {adj} {noun} just {verb} down the road.'
	
	return page_string

# if __name__ == "__main__":
app.run(host='0.0.0.0', port=1337)