from Localization.Language import Language


class Japanese(Language):
    def __init__(self):
        super().__init__(
            "日本語",
            play="あそぶ",
            settings="設定",
            back="返す",
            guest="客",
            username="ユーザー名",
            create_guest="客を作ります",
            login="ログイン",
            login_not_available="ログインを出来ません。。。",
            audio="音響",
            graphics="グラフィックス",
            music="歌",
            music_volume="歌の音量",
            sound="音",
            sound_volume="音の音量",
            volume="音量",
            fullscreen="フールスクリン",
            extra_ui_info="追加のUI情報",
            apply="適用する",
            applied_settings="設定を適用しました"
        )