from telegram import Bot, User

class Chatterbot:
	def __init__(self, token):
		logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO,
        )
        self.logger = logging.getLogger("LOG")
        self.app = Bot(token)
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher

        start_handler = CommandHandler("start", self.start)
        self.dispatcher.add_handler(start_handler)

        add_repo_handler = CommandHandler("add_repo", self.add_repo)
        self.dispatcher.add_handler(add_repo_handler)

        remove_repo_handler = CommandHandler("remove_repo", self.remove_repo)
        self.dispatcher.add_handler(remove_repo_handler)

        update_handler = CommandHandler("update", self.update)
        self.dispatcher.add_handler(update_handler)

        run_handler = CommandHandler("run", self.run)
        self.dispatcher.add_handler(run_handler)

        download_handler = CommandHandler("download", self.download)
        self.dispatcher.add_handler(download_handler)

    def start(self, bot, update):
        """
        Start command to receive /start message on Telegram.
        """
        name = update.message["chat"]["first_name"]
        start_text = (
            f"Olá {name}, eu sou o Rabot."
            "\nUm robô bem simpático criado para alegrar seu dia!\n"
        )
        bot.send_message(chat_id=update.message.chat_id, text=start_text)
        start_text = (
            "Se quiser saber mais sobre mim ou meus criadores "
            "basta digitar `/info` ;)"
        )
        bot.send_message(
            chat_id=update.message.chat_id,
            text=start_text,
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
        start_text = "Agora vamos lá. Em que posso ajudá-lo?"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=start_text,
            reply_markup=telegram.ReplyKeyboardRemove()
        )
        return 0

    def add_repo(self, bot, update):
    	pass

    def remove_repo(self, bot, update):
    	pass

    def update(self, bot, update):
    	pass

    def run(self, bot, update):
    	pass

    def download(self, bot, update):
    	pass

    def check_admin_permission(self, admin, admin_file="admin.txt"):
    	with open(admin_file, 'r') as adm_file:
    		all_adms = adm_file.read().splitlines()
    		if admin in all_adms:
    			return True
    	return False

    def check_user_permission(self, user, user_file="user.txt"):
    	with open(user_file, 'r') as usr_file:
    		all_usrs = usr_file.read().splitlines()
    		if user in all_usrs:
    			return True
    	return check_admin_permission(user)


if __name__ == "__main__":
    # Variables set on Heroku
    TOKEN = os.environ.get("TOKEN")
    NAME = os.environ.get("NAME")
    # Port is given by Heroku
    PORT = os.environ.get("PORT")
    if TOKEN is not None:
        bot = Chatterbot(TOKEN)
        bot.updater.start_webhook(
            listen="0.0.0.0",
            port=int(PORT),
            url_path=TOKEN)
        bot.updater.bot.set_webhook(f"https://{NAME}.herokuapp.com/{TOKEN}")
        bot.updater.idle()

    # Run on local system once detected that it's not on Heroku
    else:
        try:
            token = retrieve_default("TELEGRAM")["token"]
            x = Chatterbot(token)
            x.run()
        except FileNotFoundError:
            print("Configuration file not found.")
            sys.exit(1)