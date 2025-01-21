from dotenv import load_dotenv

from src.infra.config.setup import create_app
from src.infra.config.middlewares import set_middlewares


load_dotenv()

app = create_app()

set_middlewares(app)

if __name__ == "__main__":
    app.run(debug=True)








