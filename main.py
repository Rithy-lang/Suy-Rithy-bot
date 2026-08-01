import os

def main():
    # ទាញយក Token ពី Environment Variable
    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        print("Error: រកមិនឃើញ BOT_TOKEN ទេ!")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    ...
