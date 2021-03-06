import webapp2
import os
import jinja2

template_dir=os.path.dirname(__file__)
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)


class handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))


class mainpage(handler):
	def get(self):
		self.redirect("/rot13")

class ConverterPage(handler):
	def get(self):
		y=""
		text=self.request.get("form_input")
		if text:
			y=text.encode('rot13')
		self.render("gurjothtml.html",n=y)


app=webapp2.WSGIApplication([('/',mainpage),('/rot13',ConverterPage)],debug=True)
