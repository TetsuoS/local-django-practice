# local-django-practice

# モデルフォームの利用（手順）
① アプリの作成
② アプリの登録
③ URL #project/urls.py   #formdemo/urls.py
④ モデル作成　# formdemo/models.py
⑤ モデルをデータベースに反映  makemigrations    migrate
⑥ モデルフォームを作成 forms.py
⑦ URL定義の作成
⑧ ビュー作成
⑨ テンプレートファイル・HTMLファイル作成（最初は空でも良い？） /templates/formdemo　フォルダ
⑩ $ python manage.py runserver で /formdemo　にアクセスしてチェックする
