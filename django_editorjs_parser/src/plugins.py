

class Plugins:

    @staticmethod
    def header(block):
        data = block['data']
        return f"<h{data['level']}>{data['text']}</h{data['level']}>"

    @staticmethod
    def list(block):
        data = block['data']
        type_of_list = "ol" if data['style'] == "ordered" else "ul"

        html_list = [f"<li> {item} </li>" for item in data['items']]

        return f"<{type_of_list}> {' '.join(map(str,html_list))} </{type_of_list}>"
    
    @staticmethod
    def table(block):
        return 0

