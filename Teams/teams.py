import pymsteams

class Teams:

    def __init__(self, hook):
        self.hook = hook
        self.message = None
        self.teams = None
        try:
            self.teams = pymsteams.connectorcard(self.hook)
        except Exception as e:
            err = e
            raise err


    def send_message(self, message):
        self.message = str(message)
        print(self.message)
        try:
            self.teams.text(self.message)
            self.teams.send()
        except Exception as e:
            err = e
            raise err



# teams = pymsteams.connectorcard("https://nokia.webhook.office.com/webhookb2/8328fe42-ea81-45cc-826c-8b8e71d7d8b4@5d471751-9675-428d-917b-70f44f9630b0/IncomingWebhook/31c2df7431e44b3795de7b086cfc8c3e/3df53283-084d-4f22-b73d-acc44a4a3928")
# teams.text("Test")
# teams.send()