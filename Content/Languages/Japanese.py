from Localization.Language import Language


class Japanese(Language):
    def __init__(self):
        super().__init__(
            "日本語",
            play="あそぶ",
            settings="設定",
            guest="客",
            username="ユーザー名",
            create_guest="客を作ります",
            login="ログイン",
            login_not_available="ログインを出来ません。。。"
        )