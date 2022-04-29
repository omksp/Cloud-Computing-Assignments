import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(10):
            self.response.write("Omkar CloudComputing" + '<br>')
        
        
app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
