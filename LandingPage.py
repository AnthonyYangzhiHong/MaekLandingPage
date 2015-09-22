import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("input.html")
        self.response.out.write(t.render())
app = webapp2.WSGIApplication([('/', MainHandler)],debug=True)