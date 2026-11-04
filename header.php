<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script>document.documentElement.classList.add('js');</script>
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>><?php wp_body_open(); ?>
<a class="skip-link" href="#content">本文へ移動</a>
<header class="site-header">
<div class="wrap head-inner">
<a class="brand" href="<?php echo esc_url(home_url('/')); ?>">株式会社ネット風評被害対策</a>
<button class="mobile-toggle" type="button" aria-controls="primary-navigation" aria-expanded="false" aria-label="メニューを開く"><span aria-hidden="true">☰</span><span>メニュー</span></button>
<nav class="nav" id="primary-navigation" aria-label="メインメニュー">
<?php if (has_nav_menu('primary')) {
  wp_nav_menu(['theme_location'=>'primary','container'=>false,'items_wrap'=>'<ul class="nav-list">%3$s</ul>']);
} else { ?>
<a href="<?php echo esc_url(home_url('/')); ?>">TOP</a>
<a href="<?php echo esc_url(home_url('/#services')); ?>">対策内容</a>
<a href="<?php echo esc_url(home_url('/#cases')); ?>">解決事例</a>
<a href="<?php echo esc_url(home_url('/#faq')); ?>">よくある質問</a>
<a href="<?php echo esc_url(home_url('/#flow')); ?>">対策までの流れ</a>
<?php } ?>
</nav>
</div>
</header>
<main id="content">