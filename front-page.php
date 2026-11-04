<?php get_header(); ?>
<section class="hero"><div class="wrap"><div class="eyebrow">REPUTATION RISK MANAGEMENT</div><h1>ネット風評被害を<br>AIとDXで解決!</h1><p>ネット上の風評被害・誹謗中傷などのお悩みを、監視から対策までワンストップで支援します。</p><a class="btn" href="#services">対策内容を見る</a></div></section>
<section class="section"><div class="wrap"><h2>監視から対策まで、スピーディにワンストップで対応。</h2><p class="lead">リスク情報の早期発見から状況分析、適切な対応まで。ブランドイメージへの影響を抑えるために継続的に支援します。</p></div></section>
<section class="section alt" id="services"><div class="wrap"><h2>対策内容</h2><p class="lead">水面下に潜む炎上リスクの早期発見から、顕在化した問題への対応まで。</p><div class="cards"><?php
$services=[['AI監視システム（Webモニタリング）','SNSや掲示板などの情報を継続的に監視し、リスクの早期把握を支援します。'],['サジェスト非表示対策','検索候補に表示されるネガティブな語句について状況を分析し、適切な対応を検討します。'],['逆AI検索対策','AI検索におけるブランド情報の見え方を分析し、情報整備を支援します。'],['関連キーワード対策','検索関連語句の影響を調査し、改善施策を検討します。'],['逆SEO対策','検索結果における情報の影響を分析し、適切な情報発信を支援します。'],['風評被害への対応','被害状況を整理し、対応方針と再発防止策を検討します。']];
foreach($services as $s){echo '<article class="card"><h3>'.esc_html($s[0]).'</h3><p>'.esc_html($s[1]).'</p></article>';}
?></div></div></section>
<section class="section" id="cases"><div class="wrap"><h2>ネット風評被害の解決事例</h2><div class="cards"><?php foreach(['飲食店','美容クリニック','不動産','教育機関'] as $name){echo '<article class="card"><h3>'.esc_html($name).'</h3><p>課題に応じた監視・情報分析・対策を支援します。</p></article>';} ?></div></div></section>
<section class="section alt" id="faq"><div class="wrap"><h2>よくある質問</h2><div class="faq"><details><summary>ネット上の風評被害対策として重要なことは何ですか？</summary><p>早期発見と状況に応じた迅速な対応が重要です。</p></details><details><summary>社内ガイドラインは必要ですか？</summary><p>投稿ルールや緊急時の対応フローを事前に定めておくことを推奨します。</p></details><details><summary>対策の効果はいつ現れますか？</summary><p>状況や施策によって異なり、一定の効果を保証するものではありません。</p></details></div></div></section>
<section class="section" id="flow"><div class="wrap"><h2>対策導入までの流れ</h2><?php foreach(['無料リスク調査のご相談','状況の確認・ヒアリング','対策プランとお見積り','対策実施と継続的な監視'] as $i=>$step){echo '<div class="step"><strong>STEP '.esc_html($i+1).'　'.esc_html($step).'</strong></div>';} ?></div></section>
<?php get_footer(); ?>