class Survey():
    def __init__(self, question):
        self.question = question
        self.respones = []
    def show_question(self):
        print(self.question)
    def show_res(self):
        print('results')
        for response in self.respones:
            print(' - ' + response)
    def store_resp(self, response):
        self.respones.append(response)
