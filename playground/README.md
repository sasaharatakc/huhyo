# WordPress無料テスト環境

[WordPressを起動する](https://playground.wordpress.net/?blueprint-url=https%3A%2F%2Fraw.githubusercontent.com%2Fsasaharatakc%2Fhuhyo%2Fmain%2Fplayground%2Fblueprint.json)

GitHubのBlueprintからWordPress Playgroundを起動します。PHP 8.3、最新WordPress、管理画面へ自動ログイン。Elementor・フォームは導入しません。

これはブラウザ内で動く独立したテスト環境です。共有サーバーではなく、閲覧者ごとに別のWordPressが起動します。変更はGitHubへ自動保存されません。重要な変更はPlaygroundからZIPで書き出して保存してください。

現時点では新規WordPressの基盤のみ。元サイトの全ページと専用テーマは未導入です。

実装順序: 静的ソース照合 → Elementor非依存テーマ化 → 記事・画像インポート → テーマインストール検証 → 表示・編集・スマホ検証 → ZIP納品。
