from __future__ import annotations

from collections import defaultdict
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

DIRECTORIES = [
    "src/ws01",
    "src/ws02",
    "src/ws03",
    "src/ws04",
    "src/ws05",
    "src/ws07",
    "src/ws08",
    "src/ws09",
    "src/ws10",
]

PAGE_META = {
    "src/ws01": {
        "title": "ws01",
        "summary": "最初の演習で、`requests` と `BeautifulSoup` を使ってWebページ全体のHTMLを取得し、そのまま表示する最小構成です。",
        "highlights": [
            "`requests.get(url)` でURLからHTML本文を取得します。",
            "`BeautifulSoup(r.content, \"html.parser\")` でHTMLを解析可能な木構造に変換します。",
            "解析した `soup` をそのまま `print` して、タグ構造を観察するのが主目的です。",
        ],
    },
    "src/ws02": {
        "title": "ws02",
        "summary": "ローカルHTMLファイルを題材に、特定タグや `id` / `class` 条件で要素を検索する練習用ディレクトリです。",
        "highlights": [
            "`sampleTags.html` は検索対象となるサンプル文書です。",
            "`ws02.py` は `find` と `find_all` の違いを確認する導入コードです。",
            "`common.css` はHTMLサンプルの見た目を整える補助ファイルで、スクレイピング対象の属性例としても使えます。",
        ],
    },
    "src/ws03": {
        "title": "ws03",
        "summary": "ws02 の続きとして、リンク文字列・属性値・表データなど、タグの中身を実際に取り出す処理へ進んでいます。",
        "highlights": [
            "`ws03.py` はリンク、`div`、表の行列をまとめて扱う総合版です。",
            "`ws03_1.py` から `ws03_3.py` は処理を論点ごとに分割した練習用です。",
            "`.contents` を使って入れ子のタグをリストとしてたどる、基本的な木構造走査が含まれています。",
        ],
    },
    "src/ws04": {
        "title": "ws04",
        "summary": "サンプルHTMLから実サイトへ対象を移し、九州大学サイトの特定ブロックを抽出する演習です。",
        "highlights": [
            "`caution_block` や `news_block` のように、実サイトの `id` を起点に必要領域を切り出しています。",
            "HTML全体から直接探すのではなく、先に対象ブロックを絞ってから内部タグを読む構成です。",
            "ws04本体は短いコードで要点を示し、同ディレクトリ外の補助サンプルへ発展しやすい内容です。",
        ],
    },
    "src/ws05": {
        "title": "ws05",
        "summary": "Yahoo!ニュースのトップページを対象に、カテゴリリンク、トピックス、ランキングを抽出する演習です。",
        "highlights": [
            "CSSクラス名を手がかりに目的のタグを探しています。",
            "相対URLと絶対URLが混在するため、必要に応じて `urlBase` を付けています。",
            "ランキングは見出しだけでなく日付・時刻を2個1組で読み取り、表示形式を整えています。",
        ],
        "extra": [
            "このコードはCSSクラス名に強く依存するため、サイト側の更新に弱い実装です。教材としては、実サイトスクレイピングの壊れやすさを学ぶ例になっています。",
        ],
    },
    "src/ws07": {
        "title": "ws07",
        "summary": "Q-PIT のクラスタページから教員名と顔画像URLを取得し、ローカルに画像保存する演習です。",
        "highlights": [
            "教員カード全体を `teacher_list_item` で集め、名前は `fs_xxl` クラスのリンクから取得します。",
            "画像URLに対して個別に `requests.get` を送り、バイナリを書き込んで保存しています。",
            "`time.sleep(1)` を入れてアクセス間隔を空け、対象サイトへの負荷を下げています。",
        ],
    },
    "src/ws08": {
        "title": "ws08",
        "summary": "スクレイピング結果を画像保存だけで終わらせず、教員の属性情報を `pickle` で保存する段階です。",
        "highlights": [
            "`dt` と `dd` の対応を使って、職位・所属・研究テーマ・キーワードを抽出します。",
            "名前の重複を避けるために `names` リストで既出判定を行っています。",
            "`ws08.sample.py` は情報を多めに保存する完成版、`ws08.py` は職位中心に絞った短縮版です。",
        ],
    },
    "src/ws09": {
        "title": "ws09",
        "summary": "pickle で保存した教員データを再読み込みし、棒グラフとワードクラウドで可視化する演習です。",
        "highlights": [
            "保存済みの `opList.dump` を辞書 `profData` に再構成し、分析しやすい形へ変換しています。",
            "職位頻度、所属頻度、研究テーマ・キーワードのワードクラウドをそれぞれ別画像で出力します。",
            "`ws09_1.py` と `ws09_2.py` は棒グラフ部分とワードクラウド部分を分けた練習版です。",
        ],
    },
    "src/ws10": {
        "title": "ws10",
        "summary": "ここでは処理対象を1クラスタに固定せず、引数で `cluster-material` などを切り替えてデータ収集と可視化を自動実行できるようにしています。",
        "highlights": [
            "`ws10.py` はクラスタ名を受け取ってスクレイピングし、画像保存と pickle 出力を行う本体です。",
            "`ws09.py` は ws09 の可視化処理を再利用し、各クラスタ内で画像を生成するためにコピーされます。",
            "`run.sh` と `runPosPro.sh` が全クラスタを順に処理するバッチスクリプトの役目を持ちます。",
        ],
    },
}

FILE_NOTES = {
    "src/ws01/ws01.py": "Webページへアクセスし、取得したHTML全体をBeautifulSoupで解析して標準出力へ流す最小例です。",
    "src/ws02/ws02.py": "サンプルHTMLに対して `find` / `find_all` を使い、タグ・id・class を指定した検索方法を確認します。",
    "src/ws02/sampleTags.html": "BeautifulSoup の練習用に作られた小さなHTMLで、リンク、div、table など複数のタグ例を含みます。",
    "src/ws02/common.css": "サンプルHTML用のスタイルシートです。`id` や要素名が定義されており、スクレイピング対象の属性例にもなります。",
    "src/ws03/ws03.py": "リンク文字列、属性値、表セル、行の入れ子構造をまとめて読み出す総合版です。",
    "src/ws03/ws03_1.py": "リンクテキストと `href` 抽出だけに絞った最小版です。",
    "src/ws03/ws03_2.py": "`div` と `td` の読み取りを練習する中間版です。",
    "src/ws03/ws03_3.py": "`tr.contents` を2重ループでたどり、表構造を分解する例です。",
    "src/ws03/sampleTags.html": "ws02 と同じ練習用HTMLです。ws03のコードはこの静的ファイルを前提に動きます。",
    "src/ws03/common.css": "サンプルHTMLの装飾用CSSです。スクレイピングでは直接使いませんが、HTML全体の構造理解に役立ちます。",
    "src/ws04/ws04_1.py": "九州大学トップページの `caution_block` から重要なお知らせ見出しを取り出します。",
    "src/ws04/ws04_2.py": "ニュースブロックに絞って `h3`、`a`、`time` を取得する準備段階のコードです。",
    "src/ws04/demo/ws04.py": "重要なお知らせ、ニュース、数字で見る九州大学、各種ボタンリンクを一通り抽出する総合版です。",
    "src/ws04/demo/ws04_2.a.py": "ニュース一覧から日時・見出し・URLを順に出力する練習版です。",
    "src/ws04/demo/ws04_2.a2.py": "ニュース項目を `<li>` 単位でたどり、見出しと追加メタ情報を丁寧に抽出します。",
    "src/ws04/demo/ws04_3.a.py": "統計ブロックとボタンリンク一覧の抽出に焦点を当てた版です。",
    "src/ws05/ws05.py": "Yahoo!ニュースのカテゴリ、トピックス、ランキングをまとめて抽出する総合版です。",
    "src/ws05/ws05_1.py": "カテゴリボタンの取得だけに絞った版です。",
    "src/ws05/ws05_2.py": "トピックス欄のリンク抽出に絞った版です。",
    "src/ws05/ws05_3.py": "ランキング見出しと日付・時刻の対応づけに絞った版です。",
    "src/ws07/ws07.py": "Q-PITサイトから教員名と画像URLを取り出し、画像をローカル保存します。",
    "src/ws08/ws08.py": "教員名と職位を中心に収集し、pickleで `opList.dump` に保存する短縮版です。",
    "src/ws08/ws08.sample.py": "職位・所属・研究テーマ・キーワードまで含めて保存する完成版に近いサンプルです。",
    "src/ws09/ws09.py": "pickle読込、辞書再構成、棒グラフ、ワードクラウド生成を一括で行う本体です。",
    "src/ws09/ws09_1.py": "職位頻度と所属頻度の棒グラフ生成に絞った版です。",
    "src/ws09/ws09_2.py": "研究テーマ・キーワードからワードクラウドを作る部分に絞った版です。",
    "src/ws10/ws10.py": "クラスタ名を引数で受け取り、教員情報と画像をクラスタ別ディレクトリ向けに収集します。",
    "src/ws10/ws09.py": "ws09 の可視化処理をクラスタ一括処理用に再利用した版です。",
    "src/ws10/run.sh": "3クラスタに対して収集処理を順番に実行し、生成物を各クラスタディレクトリへまとめます。",
    "src/ws10/runPosPro.sh": "可視化処理と簡易HTML生成を各クラスタで実行し、比較用PNGも親ディレクトリへ集約します。",
    "src/ws10/htmlIndex.sh": "カレントディレクトリのPNG一覧をHTMLに整形するシェルスクリプトです。",
    "src/ws10/cluster-material/ws09.py": "クラスタ別にコピーされた可視化用スクリプトです。親の `src/ws10/ws09.py` とほぼ同じ役割です。",
    "src/ws10/cluster-material/htmlIndex.sh": "PNG一覧ページを自動生成するスクリプトです。",
    "src/ws10/cluster-social/ws09.py": "社会クラスタの保存済みpickleに対して可視化を行うためのスクリプトです。",
    "src/ws10/cluster-social/htmlIndex.sh": "社会クラスタ内のPNG画像一覧をHTML化します。",
    "src/ws10/cluster-system/ws09.py": "システムクラスタの保存済みpickleに対して可視化を行うためのスクリプトです。",
    "src/ws10/cluster-system/htmlIndex.sh": "システムクラスタ内のPNG画像一覧をHTML化します。",
    "src/ws10/comp/htmlIndex.sh": "比較画像を一覧表示するためのHTMLを自動生成します。",
}

FILE_DETAILS = {
    "src/ws01/ws01.py": {
        "overview": [
            "Webページへ接続し、取得したレスポンス本体を BeautifulSoup で解析して、その結果を丸ごと表示する導入用プログラムです。",
            "URLを書き換えるだけで別サイトにもアクセスできるようにしてあり、スクレイピングの最初の入口を確認する目的があります。",
        ],
        "syntax": [
            "`import requests` と `from bs4 import BeautifulSoup` は外部ライブラリの読み込みです。",
            "`try:` と `except:` により、通信や解析で失敗してもプログラム全体が停止せず `error` を表示します。",
            "`requests.get(url)` はHTTP GET要求を送り、`r.content` で本文のバイト列を取り出しています。",
            "`BeautifulSoup(..., \"html.parser\")` はHTML文字列を木構造として扱えるようにする定番の書き方です。",
        ],
    },
    "src/ws02/ws02.py": {
        "overview": [
            "ローカルのHTMLファイルを読み込み、指定したタグ名や属性で要素を検索する基本操作を確認するプログラムです。",
            "`find` は最初の1件、`find_all` は条件に合う全件を返すという違いを実例で学べます。",
        ],
        "syntax": [
            "`open(file, encoding='utf-8')` でUTF-8のHTMLファイルを開いています。",
            "`soup.find(\"body\")` のように文字列でタグ名を指定すると、そのタグを検索できます。",
            "`find_all(\"div\", id=\"stitle\")` や `class_=\"dummy\"` は属性条件付き検索です。`class` はPythonの予約語なので `class_` と書きます。",
            "変数名の先頭 `t` は単一タグ、`lst` はリストを意味しており、教材として役割が分かる命名になっています。",
        ],
    },
    "src/ws02/sampleTags.html": {
        "overview": [
            "BeautifulSoup の検索練習用に用意された静的HTMLです。",
            "リンク、複数の `div`、表、`id` と `class` を持つ要素が含まれており、検索条件の違いを試しやすい構成です。",
        ],
        "syntax": [
            "`<div id=\"stitle\">` のように `id` 属性を持つタグは、1つの固有要素を表すための例として使われています。",
            "`<div class=\"dummy\">` は同種要素のグループ化に使う `class` 属性の例です。",
            "`<a href=\"...\">` はリンク文字列と遷移先URLを持つ代表的なタグです。",
            "`<table>`, `<tr>`, `<th>`, `<td>` は表構造を作る基本タグで、後続演習の `.contents` 走査の素材になっています。",
        ],
    },
    "src/ws02/common.css": {
        "overview": [
            "サンプルHTMLの表示を整えるためのスタイルシートです。",
            "直接スクレイピングするコードではありませんが、HTML側にどの `id` や要素名が存在するかを把握する助けになります。",
        ],
        "syntax": [
            "`table { ... }` のような書き方は、要素セレクタに対してスタイルを当てるCSSの基本形です。",
            "`div#title` は `div` タグのうち `id=\"title\"` を持つ要素だけに適用されます。",
            "`background`, `color`, `font-size`, `padding` などは見た目を制御する代表的なCSSプロパティです。",
            "`/* ... */` はCSSコメントで、教材では設定のオンオフを試しやすい形になっています。",
        ],
    },
    "src/ws03/ws03.py": {
        "overview": [
            "リンク抽出、`div` の内容取得、表セルと表行の走査を1本にまとめた総合的な練習コードです。",
            "BeautifulSoup のタグオブジェクトから `.string`、`.get()`、`.contents` をどう使い分けるかが分かります。",
        ],
        "syntax": [
            "`lstA[0].string` はタグで囲まれた文字列本体を取得する書き方です。",
            "`lstA[0].get(\"href\")` は属性値を取得する定番パターンです。",
            "`for i in range(len(lstTr)):` のようなループで、リスト内の各タグを順番に処理しています。",
            "二重ループにより `tr` の中にある各 `td` をたどり、HTMLの入れ子構造を段階的に分解しています。",
        ],
    },
    "src/ws03/ws03_1.py": {
        "overview": [
            "リンクテキストとリンク先URLだけに注目した短い練習コードです。",
            "大きなHTML解析の前に、タグ1種類だけを安全に扱う練習として位置付けられます。",
        ],
        "syntax": [
            "`find_all(\"a\")` で全リンクを取得し、その先頭要素に対して処理しています。",
            "添字 `lstA[0]` はリストの最初の要素を参照するPythonの基本記法です。",
            "文字列取得に `.string`、属性取得に `.get(\"href\")` を使う対比が明確です。",
        ],
    },
    "src/ws03/ws03_2.py": {
        "overview": [
            "`div` と `td` のテキスト抽出に絞り、タグ検索と単純な繰り返し処理を確認するコードです。",
            "複数件ヒットする要素に対して順番に `print` する基本形が学べます。",
        ],
        "syntax": [
            "`find_all` の返り値はリストなので、`len(...)` と `range(...)` を組み合わせて走査しています。",
            "`.string` はタグ内が単純なテキストだけである場合に素直に値を返します。",
            "`print(i, value)` の形は、添字と内容を同時に確認するデバッグ向きの書き方です。",
        ],
    },
    "src/ws03/ws03_3.py": {
        "overview": [
            "表の行 `tr` を起点に、その子要素を `.contents` で直接たどる構造解析の練習コードです。",
            "スクレイピングで重要な「親から子へ」「リストから個別へ」という見方を強調しています。",
        ],
        "syntax": [
            "`.contents` はタグ直下の子要素をPythonリストとして返します。",
            "二重ループにより、外側で行、内側でセルという2段階の入れ子を処理しています。",
            "`lstTr[i].contents[j].contents` のように連鎖させると、さらに深い階層へ進めます。",
        ],
    },
    "src/ws03/sampleTags.html": {
        "overview": [
            "ws02 と同じ練習用HTMLで、ws03ではこの中のリンクや表を読み出す対象として使います。",
        ],
        "syntax": [
            "タグ構造そのものはws02と同じで、BeautifulSoupが返す結果を確認する教材になっています。",
        ],
    },
    "src/ws03/common.css": {
        "overview": [
            "サンプルHTMLの見た目を整えるCSSです。",
        ],
        "syntax": [
            "要素セレクタ、IDセレクタ、コメント構文など、HTML理解に関係するCSSの基本が含まれています。",
        ],
    },
    "src/ws04/ws04_1.py": {
        "overview": [
            "九州大学サイトの `caution_block` に限定して情報を抽出する、実サイト向け最初の例です。",
            "HTML全体から探すのではなく、先に大きなブロックを絞る考え方を学べます。",
        ],
        "syntax": [
            "`urlBase` と `url` を分けることで、基底URLとアクセス先URLの役割を整理しています。",
            "`find_all(\"div\", id=\"caution_block\")` で目的ブロックを取得した後、さらにその中で `find_all(\"h3\")` を呼んでいます。",
            "このような段階検索は、対象範囲を狭めて誤検出を減らすスクレイピングの基本です。",
        ],
    },
    "src/ws04/ws04_2.py": {
        "overview": [
            "ニュースブロックを抽出し、後続処理で使う見出し、リンク、日時タグを個別に取り出す準備コードです。",
        ],
        "syntax": [
            "`lstDivId[0].find_all(...)` の形で、見つけたブロックの内部だけを検索しています。",
            "`find` と `find_all` の候補がコメントで残っており、1件だけ欲しい場合と全件欲しい場合の違いが見えます。",
        ],
    },
    "src/ws04/demo/ws04.py": {
        "overview": [
            "九州大学トップページから複数種類の情報を一度に抜き出す総合版です。",
            "見出し抽出、日時とURLの組み合わせ、数値文字列の整数化、重複除去など、スクレイピングの実務的な要素がまとまっています。",
        ],
        "syntax": [
            "`news_url=lstACl[i].get(\"href\")` の後で `urlBase + news_url[1:]` としているのは、先頭の `/` を落として基底URLへ連結するためです。",
            "`int(lstP[i].string.replace(\",\", \"\"))` はカンマ付き数値文字列を整数へ変換する典型例です。",
            "`if(tl not in lstTl):` は重複タイトルを避ける条件分岐です。",
            "コメントアウトされた `print` が多く、途中結果を確認しながら開発した流れが読み取れます。",
        ],
    },
    "src/ws04/demo/ws04_2.a.py": {
        "overview": [
            "ニュース一覧から日時、見出し、リンクを順に出力するシンプルな版です。",
        ],
        "syntax": [
            "同じ添字 `i` で `lstH3Cl`, `lstACl`, `lstTime` を対応づけて処理しています。",
            "複数リストの位置対応を前提にするのは簡単ですが、HTML構造が変わると崩れやすいという注意点もあります。",
        ],
    },
    "src/ws04/demo/ws04_2.a2.py": {
        "overview": [
            "ニュース項目を `<li>` 単位で見て、要素ごとのまとまりを崩さず情報を読む、より堅い書き方の例です。",
        ],
        "syntax": [
            "`tH3Local=lstLi[i].find(\"h3\")` のように、各リスト項目を局所的な探索範囲にしています。",
            "`if(len(lstH5Local) != 0):` で追加情報の有無を確認してからアクセスしており、空リスト対策になっています。",
            "リスト内包表記 `pi=[j.string for j in lstH5Local]` は複数要素の文字列抽出を簡潔に書く文法です。",
        ],
    },
    "src/ws04/demo/ws04_3.a.py": {
        "overview": [
            "統計値ブロックとボタンリンクの一覧化に焦点を絞った版です。",
        ],
        "syntax": [
            "`tDivId.find(\"ul\", class_=\"body\")` のように、親タグからさらに条件付きで子タグを検索しています。",
            "`lstH3[i].contents[0]` はタグ内の先頭テキストノードを取り出しています。",
            "重複除去には `lstTl` と `lstLink` を並行して使う単純な手法を採用しています。",
        ],
    },
    "src/ws05/ws05.py": {
        "overview": [
            "Yahoo!ニュースのトップページからカテゴリ、トピックス、ランキングをまとめて取得する実サイト向け演習です。",
            "CSSクラス名依存のスクレイピングがサイト更新で壊れやすいことも読み取れる教材です。",
        ],
        "syntax": [
            "`if(\"https:\" not in link):` で相対URLかどうかを判定し、必要なら基底URLを付けています。",
            "ランキングでは `j=i*2` として、日付と時刻が2要素ずつ並ぶリストから対応する値を拾っています。",
            "コメントで `As of 2024/4/23` のように時点が書かれており、クラス名が時期によって変わる前提が示されています。",
        ],
    },
    "src/ws05/ws05_1.py": {
        "overview": [
            "Yahoo!ニュース上部のカテゴリボタン抽出だけを扱う簡易版です。",
        ],
        "syntax": [
            "リンクのテキストと `href` を取り出し、相対URLだけ補正する基本パターンです。",
        ],
    },
    "src/ws05/ws05_2.py": {
        "overview": [
            "トピックス欄のリンク群だけを取り出す簡易版です。",
        ],
        "syntax": [
            "`lstACl[i].contents[0]` はリンク内の先頭内容を取り出す書き方で、`.string` より少し低レベルな参照です。",
        ],
    },
    "src/ws05/ws05_3.py": {
        "overview": [
            "ランキング見出しと日時を対応づける処理に集中した版です。",
        ],
        "syntax": [
            "見出しリストと日時リストの長さ・並び順が対応している前提で、算術的に添字を計算しています。",
        ],
    },
    "src/ws07/ws07.py": {
        "overview": [
            "教員一覧ページから名前と画像URLを取得し、画像ファイルとして保存する収集プログラムです。",
            "テキスト抽出だけでなく、HTTPレスポンスのバイナリ保存まで扱う点が前半演習との違いです。",
        ],
        "syntax": [
            "`requests.get(src, allow_redirects=False)` は画像URLへ直接アクセスしてデータを取得する書き方です。",
            "`open(fn, \"wb\")` の `wb` はバイナリ書き込みモードを意味します。",
            "`src.split(\".\")[-1]` は拡張子だけを末尾から取り出すPythonの定番表現です。",
            "`time.sleep(1)` で1秒待機し、連続アクセスを緩和しています。",
        ],
    },
    "src/ws08/ws08.py": {
        "overview": [
            "教員名と職位を抽出し、後で再利用できるよう `pickle` 形式で保存するプログラムです。",
            "HTMLの都度解析から、構造化データ保存へ進む段階に当たります。",
        ],
        "syntax": [
            "`pickle.dump(opList, f)` はPythonオブジェクトをバイナリ形式で保存する文法です。",
            "`cat=[j.string for j in lstDt]` はリスト内包表記で、タグ群から文字列だけを抜き出しています。",
            "`if name not in names:` によって重複登録を防いでいます。",
        ],
    },
    "src/ws08/ws08.sample.py": {
        "overview": [
            "職位に加えて所属、研究テーマ、キーワードまで含めて保存する完成版サンプルです。",
            "後続の可視化で必要になる情報がここで一通り揃います。",
        ],
        "syntax": [
            "カテゴリ名 `cat[k]` に応じて `jtl`, `afl`, `theme`, `key` へ振り分ける分岐が中心です。",
            "`tmp.append(...)` を順番に並べることで、後段で固定位置のデータとして読み出せるようにしています。",
        ],
    },
    "src/ws09/ws09.py": {
        "overview": [
            "保存済みの教員データを読み戻し、棒グラフとワードクラウドを生成する可視化プログラムです。",
            "データ収集と分析処理が分離されている点が、この演習全体の重要な構成です。",
        ],
        "syntax": [
            "`profData={'name':[], ...}` のような辞書で項目別リストを管理しています。",
            "`list(set(jbtList))` は重複を除いたカテゴリ一覧を作る表現です。",
            "`plt.bar(...)`, `plt.grid()`, `plt.savefig(...)` は matplotlib の基本的な描画手順です。",
            "`WordCloud(...).generate(txt)` で文字列からワードクラウド画像を生成しています。",
            "`mask=255-mask` は画像の白黒を反転させて、雲の形状マスクとして使いやすくする処理です。",
        ],
    },
    "src/ws09/ws09_1.py": {
        "overview": [
            "棒グラフによる頻度集計だけを抜き出した版です。",
        ],
        "syntax": [
            "辞書 `data` にカテゴリごとの件数を入れ、`values()` を棒グラフの高さに使っています。",
        ],
    },
    "src/ws09/ws09_2.py": {
        "overview": [
            "ワードクラウド生成部分だけを抜き出した版です。",
        ],
        "syntax": [
            "`filter(None, profData['keywords'])` は空要素を取り除く書き方です。",
            "フォントパスを明示しているのは、日本語文字を正しく描画するためです。",
        ],
    },
    "src/ws10/ws10.py": {
        "overview": [
            "クラスタ名を引数で受け取り、対象ページを切り替えながら教員情報と画像を収集する汎用版です。",
            "ws08 をベースにしつつ、処理対象の一般化と画像保存の両方を担っています。",
        ],
        "syntax": [
            "`args = sys.argv` と `clusterName=args[1]` はコマンドライン引数の受け取りです。",
            "`url=urlBase+clusterName+\"/\"` により、引数から対象URLを組み立てています。",
            "`j.text` を使っている箇所は、`.string` だと扱いにくい入れ子要素込みのテキストを安全に取るためです。",
            "画像保存ループとプロフィール保存処理が同じ `for i in range(len(lstDivCl)):` に入っており、1人分ずつまとめて処理する構成です。",
        ],
    },
    "src/ws10/ws09.py": {
        "overview": [
            "クラスタ別ディレクトリで再利用するために調整された可視化スクリプトです。",
            "ws09 とほぼ同じ処理ですが、途中の表示を減らし、バッチ実行向けになっています。",
        ],
        "syntax": [
            "`plt.show()` がコメントアウトされており、対話表示ではなくファイル保存中心の実行を意図しています。",
            "辞書再構成、頻度集計、ワードクラウド生成の流れは ws09 本体と同じです。",
        ],
    },
    "src/ws10/run.sh": {
        "overview": [
            "3つのクラスタを順番に処理し、収集結果をクラスタ別フォルダへまとめるシェルスクリプトです。",
        ],
        "syntax": [
            "`CLIST=\"cluster-material cluster-system cluster-social\"` は空白区切りのリスト変数です。",
            "`for c in $CLIST` で各クラスタ名を順番に処理しています。",
            "`if [ -e $c ]` は対象パスの存在確認、`mkdir figs` は出力先作成です。",
            "`mv figs $c` と `mv opList.dump $c` で生成物をクラスタ名のディレクトリへ移しています。",
        ],
    },
    "src/ws10/runPosPro.sh": {
        "overview": [
            "収集済みクラスタごとに可視化処理と簡易HTML生成を行い、比較用PNGも親ディレクトリへ集約する後処理スクリプトです。",
        ],
        "syntax": [
            "`cp ws09.py brain.png htmlIndex.sh $c` で必要ファイルを各クラスタへコピーしています。",
            "`cd $c` でディレクトリ移動し、その場で `python3.9 ws09.py` を実行します。",
            "`cp wc.png ../${c}.png` は変数展開 `${c}` を用いて親ディレクトリへクラスタ名付き画像を保存する書き方です。",
        ],
    },
    "src/ws10/htmlIndex.sh": {
        "overview": [
            "カレントディレクトリ内のPNG画像を表形式で並べた簡易HTMLを自動生成するスクリプトです。",
        ],
        "syntax": [
            "`HF=\"./index.html\"` のような代入で出力先ファイルを定義しています。",
            "`echo '...' > ${HF}` と `>>` は、それぞれ上書き出力と追記出力です。",
            "`for i in ${DN2}/*${SUFFIX2}` はPNGファイル群を順に処理するシェルのグロブ展開です。",
            "`if [[ \\`expr $j % $R\\` -eq 0 ]]` で列数に応じて改行位置を切り替えています。",
        ],
    },
    "src/ws10/cluster-material/ws09.py": {
        "overview": [
            "材料クラスタ向けの保存済みデータを可視化するために配置されたスクリプトです。",
        ],
        "syntax": [
            "構文自体は `src/ws10/ws09.py` と同系統で、pickle読込と可視化の流れをそのまま使います。",
        ],
    },
    "src/ws10/cluster-material/htmlIndex.sh": {
        "overview": [
            "材料クラスタ内のPNGを一覧表示するHTMLを生成します。",
        ],
        "syntax": [
            "シェル変数、`for` ループ、`echo` によるHTML組み立てという基本文法で構成されています。",
        ],
    },
    "src/ws10/cluster-social/ws09.py": {
        "overview": [
            "社会クラスタの可視化処理を行うスクリプトです。",
        ],
        "syntax": [
            "構文の骨格は `src/ws10/ws09.py` と同じで、データだけが社会クラスタのものに変わります。",
        ],
    },
    "src/ws10/cluster-social/htmlIndex.sh": {
        "overview": [
            "社会クラスタ内のPNG一覧HTMLを生成します。",
        ],
        "syntax": [
            "PNG列挙、表セル生成、出力ファイルへの追記というシェルの基本構文で構成されています。",
        ],
    },
    "src/ws10/cluster-system/ws09.py": {
        "overview": [
            "システムクラスタの可視化処理を行うスクリプトです。",
        ],
        "syntax": [
            "可視化の文法や処理順は `src/ws10/ws09.py` と共通です。",
        ],
    },
    "src/ws10/cluster-system/htmlIndex.sh": {
        "overview": [
            "システムクラスタ内のPNG一覧HTMLを生成します。",
        ],
        "syntax": [
            "ファイル列挙と `echo` によるHTML生成という単純なシェル文法で書かれています。",
        ],
    },
    "src/ws10/comp/htmlIndex.sh": {
        "overview": [
            "比較用PNGを並べるHTMLを生成する補助スクリプトです。",
        ],
        "syntax": [
            "親ディレクトリの `htmlIndex.sh` と同様に、変数、ループ、条件分岐を使ってHTML文字列を出力しています。",
        ],
    },
}

CODE_EXTS = {".py", ".sh", ".css"}
HTML_SOURCE_FILES = {
    "src/ws02/sampleTags.html",
    "src/ws03/sampleTags.html",
}
PAGE_FILENAMES = {directory: f"doc_{directory.replace('/', '_')}.html" for directory in DIRECTORIES}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def source_files_for(directory: str) -> list[Path]:
    dir_path = ROOT / directory
    files: list[Path] = []
    for path in sorted(dir_path.iterdir()):
        rel = path.relative_to(ROOT).as_posix()
        if path.is_file() and (path.suffix in CODE_EXTS or rel in HTML_SOURCE_FILES):
            files.append(path)
    return files


def asset_summary(directory: str) -> list[str]:
    dir_path = ROOT / directory
    counts: dict[str, int] = defaultdict(int)
    for path in dir_path.iterdir():
        if path.is_file():
            rel = path.relative_to(ROOT).as_posix()
            if path.suffix in CODE_EXTS or rel in HTML_SOURCE_FILES:
                continue
            suffix = path.suffix.lower() or "[拡張子なし]"
            counts[suffix] += 1
    summary = []
    for suffix, count in sorted(counts.items()):
        summary.append(f"{suffix} ファイル: {count} 件")
    return summary


def children_of(directory: str) -> list[str]:
    prefix = f"{directory}/"
    depth = directory.count("/")
    return [
        child for child in DIRECTORIES
        if child.startswith(prefix) and child.count("/") == depth + 1
    ]


def nav_links(current: str) -> str:
    items = []
    for directory in DIRECTORIES:
        label = PAGE_META[directory]["title"]
        href = PAGE_FILENAMES[directory]
        cls = "current" if directory == current else ""
        items.append(f'<a class="{cls}" href="{href}">{escape(label)}</a>')
    return "\n".join(items)


def render_file_block(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    note = FILE_NOTES.get(rel, "このファイルの役割をページ生成時に自動掲載しています。")
    details = FILE_DETAILS.get(rel, {})
    overview_items = "".join(f"<li>{escape(item)}</li>" for item in details.get("overview", []))
    syntax_items = "".join(f"<li>{escape(item)}</li>" for item in details.get("syntax", []))
    code = escape(read_text(path))
    return f"""
    <section class="file-block">
      <h3>{escape(rel)}</h3>
      <p class="note">{escape(note)}</p>
      <pre><code>{code}</code></pre>
      <div class="explain">
        <h4>プログラムの概要</h4>
        {f'<ul>{overview_items}</ul>' if overview_items else '<p>このファイルの役割を簡潔に示す解説をここに追加します。</p>'}
        <h4>構文・文法のポイント</h4>
        {f'<ul>{syntax_items}</ul>' if syntax_items else '<p>主要な構文や文法の説明をここに追加します。</p>'}
      </div>
    </section>
    """


def render_directory_page(directory: str) -> str:
    meta = PAGE_META[directory]
    title = meta["title"]
    source_files = source_files_for(directory)
    child_dirs = children_of(directory)
    assets = asset_summary(directory)

    file_blocks = "\n".join(render_file_block(path) for path in source_files)
    source_link_items = "\n".join(
        (
            f'<li><a href="{escape(path.relative_to(ROOT).as_posix())}" download>'
            f'{escape(path.name)}</a></li>'
        )
        for path in source_files
    )
    highlight_items = "\n".join(f"<li>{escape(item)}</li>" for item in meta.get("highlights", []))
    extra_items = "\n".join(f"<li>{escape(item)}</li>" for item in meta.get("extra", []))
    asset_items = "\n".join(f"<li>{escape(item)}</li>" for item in assets)

    files_html = file_blocks or "<p>このディレクトリには、解説対象とするソースコードファイルはありません。</p>"
    source_links_html = (
        f"<ul>{source_link_items}</ul>"
        if source_link_items else
        "<p>このディレクトリには、配布対象のソースコードファイルはありません。</p>"
    )
    extra_html = f"<ul>{extra_items}</ul>" if extra_items else ""

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} の解説</title>
  <style>
    :root {{
      --bg: #f4f1ea;
      --paper: #fffdf9;
      --ink: #22201d;
      --sub: #5d574f;
      --line: #d6c8b2;
      --accent: #8b5e34;
      --accent-soft: #efe3d2;
      --code: #2b241d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Hiragino Sans", "Yu Gothic", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, #f8ead1 0, transparent 30%),
        linear-gradient(180deg, #f6f2eb 0%, #efe6da 100%);
      line-height: 1.7;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr);
      min-height: 100vh;
    }}
    nav {{
      padding: 24px 18px;
      border-right: 1px solid var(--line);
      background: rgba(255, 253, 249, 0.82);
      backdrop-filter: blur(10px);
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
    }}
    nav h1 {{
      margin: 0 0 14px;
      font-size: 1.1rem;
    }}
    nav p {{
      margin: 0 0 14px;
      color: var(--sub);
      font-size: 0.92rem;
    }}
    nav a {{
      display: block;
      padding: 8px 10px;
      margin-bottom: 6px;
      border-radius: 10px;
      color: var(--ink);
      text-decoration: none;
      background: transparent;
    }}
    nav a.current {{
      background: var(--accent-soft);
      color: #5a391c;
      font-weight: 700;
    }}
    nav a:hover {{
      background: #f1e7d9;
    }}
    main {{
      padding: 32px;
    }}
    .hero {{
      background: rgba(255, 253, 249, 0.9);
      border: 1px solid var(--line);
      border-radius: 24px;
      padding: 28px;
      box-shadow: 0 16px 40px rgba(82, 59, 29, 0.08);
    }}
    .eyebrow {{
      margin: 0 0 8px;
      color: var(--accent);
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-size: 0.8rem;
    }}
    h2 {{
      margin: 0 0 12px;
      font-size: clamp(1.8rem, 2.8vw, 2.6rem);
      line-height: 1.2;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 20px;
      margin-top: 24px;
    }}
    .card, .file-block {{
      background: rgba(255, 253, 249, 0.92);
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 22px;
      margin-top: 22px;
      box-shadow: 0 12px 30px rgba(82, 59, 29, 0.06);
    }}
    .card h3, .file-block h3 {{
      margin-top: 0;
      margin-bottom: 12px;
      font-size: 1.15rem;
    }}
    .file-block h4 {{
      margin: 18px 0 10px;
      font-size: 1rem;
      color: #6b4322;
    }}
    ul {{
      margin: 0;
      padding-left: 1.2rem;
    }}
    .note {{
      color: var(--sub);
      margin-bottom: 14px;
    }}
    pre {{
      margin: 0;
      padding: 18px;
      overflow: auto;
      border-radius: 16px;
      background: var(--code);
      color: #f7f2ea;
      font-size: 0.9rem;
      line-height: 1.5;
    }}
    code {{
      font-family: "SFMono-Regular", Consolas, monospace;
    }}
    .explain {{
      margin-top: 18px;
      padding-top: 8px;
      border-top: 1px solid var(--line);
    }}
    a.inline {{
      color: var(--accent);
    }}
    @media (max-width: 960px) {{
      .layout {{
        grid-template-columns: 1fr;
      }}
      nav {{
        position: static;
        height: auto;
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }}
      main {{
        padding: 20px;
      }}
      .grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <nav>
      <h1>src 解説ページ</h1>
      <p><a class="inline" href="index.html">目次へ戻る</a></p>
      {nav_links(directory)}
    </nav>
    <main>
      <section class="hero">
        <p class="eyebrow">Directory Guide</p>
        <h2>{escape(title)}</h2>
        <p>{escape(meta['summary'])}</p>
      </section>

      <div class="grid">
        <section class="card">
          <h3>読みどころ</h3>
          <ul>{highlight_items}</ul>
        </section>
        <section class="card">
          <h3>ソースコード一覧</h3>
          {source_links_html}
        </section>
      </div>
      {f'<section class="card"><h3>補足</h3>{extra_html}</section>' if extra_html else ''}
      {files_html}
    </main>
  </div>
</body>
</html>
"""


def render_index() -> str:
    cards = []
    for directory in DIRECTORIES:
        meta = PAGE_META[directory]
        cards.append(
            f"""
            <a class="card" href="{PAGE_FILENAMES[directory]}">
              <p class="path">{escape(directory)}</p>
              <h2>{escape(meta['title'])}</h2>
              <p>{escape(meta['summary'])}</p>
            </a>
            """
        )
    cards_html = "\n".join(cards)
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>融合応用情報学C - 融合基礎工学科</title>
  <style>
    :root {{
      --bg: #f5efe6;
      --paper: rgba(255, 251, 245, 0.92);
      --ink: #211d19;
      --sub: #5b5349;
      --line: #d8c7af;
      --accent: #9f5126;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Hiragino Sans", "Yu Gothic", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 10% 10%, #f6d9b8 0, transparent 20%),
        radial-gradient(circle at 90% 20%, #ead8bf 0, transparent 24%),
        linear-gradient(180deg, #f8f2ea 0%, #efe4d4 100%);
    }}
    main {{
      width: min(1180px, calc(100% - 32px));
      margin: 0 auto;
      padding: 40px 0 56px;
    }}
    .hero {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 28px;
      padding: 30px;
      box-shadow: 0 18px 44px rgba(91, 63, 35, 0.08);
      margin-bottom: 24px;
    }}
    .hero p {{
      max-width: 54rem;
    }}
    h1 {{
      margin: 0 0 12px;
      font-size: clamp(2rem, 4vw, 3.6rem);
      line-height: 1.1;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }}
    .card {{
      display: block;
      text-decoration: none;
      color: inherit;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 22px;
      padding: 22px;
      min-height: 200px;
      box-shadow: 0 10px 30px rgba(91, 63, 35, 0.06);
      transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }}
    .card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 18px 34px rgba(91, 63, 35, 0.12);
      border-color: #c89870;
    }}
    .path {{
      margin: 0 0 10px;
      color: var(--accent);
      font-weight: 700;
      font-size: 0.85rem;
      letter-spacing: 0.04em;
    }}
    h2 {{
      margin: 0 0 10px;
      font-size: 1.25rem;
    }}
    p {{
      margin: 0;
      line-height: 1.7;
      color: var(--sub);
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>融合応用情報学C - 融合基礎工学科</h1>
      <p>この目次は、`src` 配下の各ディレクトリごとに作成した日本語の解説ページへ移動するための入口です。前半はWebスクレイピングの基本、後半はデータ保存・可視化・クラスタ別処理という流れが追えるように構成しています。</p>
    </section>
    <section class="grid">
      {cards_html}
    </section>
  </main>
</body>
</html>
"""


def main() -> None:
    for directory in DIRECTORIES:
        output = ROOT / PAGE_FILENAMES[directory]
        output.write_text(render_directory_page(directory), encoding="utf-8")
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")


if __name__ == "__main__":
    main()
