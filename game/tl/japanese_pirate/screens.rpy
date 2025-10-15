# TODO: Translation updated at 2025-10-13 21:52

screen lang_choice:

    textbutton "Russian":
        xalign 0.5
        yalign 0.43
        action [Language(None), Return()]

    textbutton "English":
        xalign 0.5
        yalign 0.5
        action [Language("english"), Return()]

    textbutton "Japanese (Pirate)":
        xalign 0.5
        yalign 0.57
        action [Language("japanese_pirate"), Return()]

translate japanese_pirate strings:

    # game/screens.rpy:253
    old "Назад"
    new "戻る"

    # game/screens.rpy:254
    old "История"
    new "履歴"

    # game/screens.rpy:255
    old "Пропуск"
    new "スキップ"

    # game/screens.rpy:256
    old "Авто"
    new "オート"

    # game/screens.rpy:257
    old "Сохранить"
    new "セーブ"

    # game/screens.rpy:258
    old "Б.Сохр"
    new "Q.セーブ"

    # game/screens.rpy:259
    old "Б.Загр"
    new "Q.ロード"

    # game/screens.rpy:260
    old "Опции"
    new "オプション"

    # game/screens.rpy:303
    old "Начать"
    new "はじめから"

    # game/screens.rpy:311
    old "Загрузить"
    new "ロード"

    # game/screens.rpy:313
    old "Настройки"
    new "設定"

    # game/screens.rpy:317
    old "Завершить повтор"
    new "リプレイ終了"

    # game/screens.rpy:321
    old "Главное меню"
    new "メインメニュー"

    # game/screens.rpy:323
    old "Об игре"
    new "ゲームについて"

    # game/screens.rpy:328
    old "Помощь"
    new "ヘルプ"

    # game/screens.rpy:334
    old "Выход"
    new "終了"

    # game/screens.rpy:481
    old "Вернуться"
    new "戻る"

    # game/screens.rpy:565
    old "Версия [config.version!t]\n"
    new "バージョン [config.version!t]\n"

    # game/screens.rpy:571
    old "Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]で製作。\n\n[renpy.license!t]"

    # game/screens.rpy:606
    old "{} страница"
    new "{}ページ"

    # game/screens.rpy:606
    old "Автосохранения"
    new "オートセーブ"

    # game/screens.rpy:606
    old "Быстрые сохранения"
    new "クイックセーブ"

    # game/screens.rpy:649
    old "{#file_time}%A, %d %B %Y, %H:%M"
    new "{#file_time}%Y年%m月%d日 %H:%M"

    # game/screens.rpy:649
    old "Пустой слот"
    new "空きスロット"

    # game/screens.rpy:669
    old "<"
    new "<"

    # game/screens.rpy:672
    old "{#auto_page}А"
    new "{#auto_page}A"

    # game/screens.rpy:675
    old "{#quick_page}Б"
    new "{#quick_page}Q"

    # game/screens.rpy:681
    old ">"
    new ">"

    # game/screens.rpy:739
    old "Режим экрана"
    new "画面モード"

    # game/screens.rpy:740
    old "Оконный"
    new "ウィンドウ"

    # game/screens.rpy:741
    old "Полный"
    new "フルスクリーン"

    # game/screens.rpy:746
    old "Всего текста"
    new "全てのテキスト"

    # game/screens.rpy:747
    old "После выборов"
    new "選択後"

    # game/screens.rpy:748
    old "Переходов"
    new "画面切り替え"

    # game/screens.rpy:761
    old "Скорость текста"
    new "テキスト速度"

    # game/screens.rpy:765
    old "Скорость авточтения"
    new "オート速度"

    # game/screens.rpy:772
    old "Громкость музыки"
    new "音楽音量"

    # game/screens.rpy:779
    old "Громкость звуков"
    new "効果音音量"

    # game/screens.rpy:785
    old "Тест"
    new "テスト"

    # game/screens.rpy:792
    old "Без звука"
    new "ミュート"

    # game/screens.rpy:912
    old "История диалогов пуста."
    new "履歴がありません。"

    # game/screens.rpy:980
    old "Клавиатура"
    new "キーボード"

    # game/screens.rpy:981
    old "Мышь"
    new "マウス"

    # game/screens.rpy:984
    old "Геймпад"
    new "ゲームパッド"

    # game/screens.rpy:997
    old "Войти"
    new "Enter"

    # game/screens.rpy:998
    old "Прохождение диалогов, активация интерфейса."
    new "ダイアログを進め、インターフェースを有効にする。"

    # game/screens.rpy:1001
    old "Пробел"
    new "Space"

    # game/screens.rpy:1002
    old "Прохождение диалогов без возможности делать выбор."
    new "選択肢なしでダイアログを進める。"

    # game/screens.rpy:1005
    old "Стрелки"
    new "方向キー"

    # game/screens.rpy:1006
    old "Навигация по интерфейсу."
    new "インターフェースを操作する。"

    # game/screens.rpy:1009
    old "Esc"
    new "Esc"

    # game/screens.rpy:1010
    old "Вход в игровое меню."
    new "ゲームメニューを開く。"

    # game/screens.rpy:1013
    old "Ctrl"
    new "Ctrl"

    # game/screens.rpy:1014
    old "Пропускает диалоги, пока зажат."
    new "押している間ダイアログをスキップ。"

    # game/screens.rpy:1017
    old "Tab"
    new "Tab"

    # game/screens.rpy:1018
    old "Включает режим пропуска."
    new "スキップモードを有効化。"

    # game/screens.rpy:1021
    old "Страница вверху"
    new "Page Up"

    # game/screens.rpy:1022
    old "Откат назад по сюжету игры."
    new "ストーリーを巻き戻す。"

    # game/screens.rpy:1025
    old "Страница вниз"
    new "Page Down"

    # game/screens.rpy:1026
    old "Откатывает предыдущее действие вперёд."
    new "前の操作を早送りする。"

    # game/screens.rpy:1030
    old "Скрывает интерфейс пользователя."
    new "UIを非表示にする。"

    # game/screens.rpy:1034
    old "Делает снимок экрана."
    new "スクリーンショットを撮る。"

    # game/screens.rpy:1038
    old "Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}."
    new "サポートされている{a=https://www.renpy.org/l/voicing}音声合成{/a}を有効にする。"

    # game/screens.rpy:1042
    old "Открывает меню специальных возможностей."
    new "アクセシビリティメニューを開く。"

    # game/screens.rpy:1048
    old "Левый клик"
    new "左クリック"

    # game/screens.rpy:1052
    old "Клик колёсиком"
    new "ホイールクリック"

    # game/screens.rpy:1056
    old "Правый клик"
    new "右クリック"

    # game/screens.rpy:1060
    old "Колёсико вверх\nКлик на сторону отката"
    new "ホイールアップ"

    # game/screens.rpy:1064
    old "Колёсико вниз"
    new "ホイールダウン"

    # game/screens.rpy:1071
    old "Правый триггер\nA/Нижняя кнопка"
    new "RT\nA/下ボタン"

    # game/screens.rpy:1075
    old "Левый Триггер\nЛевый Бампер"
    new "LT\nLB"

    # game/screens.rpy:1079
    old "Правый бампер"
    new "RB"

    # game/screens.rpy:1084
    old "Крестовина, Стики"
    new "十字キー、スティック"

    # game/screens.rpy:1088
    old "Начало, Руководство"
    new "スタート、ガイド"

    # game/screens.rpy:1092
    old "Y/Верхняя кнопка"
    new "Y/上ボタン"

    # game/screens.rpy:1095
    old "Калибровка"
    new "キャリブレーション"

    # game/screens.rpy:1160
    old "Да"
    new "はい"

    # game/screens.rpy:1161
    old "Нет"
    new "いいえ"

    # game/screens.rpy:1207
    old "Пропускаю"
    new "スキップ中"

    # game/screens.rpy:1518
    old "Меню"
    new "メニュー"
