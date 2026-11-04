<?php
if (!defined('ABSPATH')) exit;
add_action('after_setup_theme', function () {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
  add_theme_support('html5', ['search-form','comment-form','comment-list','gallery','caption','style','script']);
  register_nav_menus(['primary'=>'Primary Navigation']);
  add_theme_support('responsive-embeds');
  add_theme_support('align-wide');
  add_theme_support('editor-styles');
  add_editor_style('style.css');
  add_theme_support('custom-logo', ['height'=>80, 'width'=>320, 'flex-width'=>true, 'flex-height'=>true]);
});
add_action('wp_enqueue_scripts', function () {
  $version = wp_get_theme()->get('Version');
  wp_enqueue_style('fuhyo-custom', get_stylesheet_uri(), [], $version);
  wp_enqueue_script('fuhyo-mobile-nav', get_template_directory_uri() . '/assets/mobile-nav.js', [], $version, true);
});
add_filter('wp_robots', function ($robots) {
  if (wp_get_environment_type() !== 'production') {
    $robots['noindex'] = true;
    $robots['nofollow'] = true;
  }
  return $robots;
});
// Register the initial editable layout once; setup.php uses the same source.
add_action('init', function () {
  $pattern_path = get_template_directory() . '/inc/home-blocks.html';
  if (function_exists('register_block_pattern') && is_readable($pattern_path)) {
    register_block_pattern('fuhyo-custom/home', [
      'title' => '風評被害対策：トップページ初期レイアウト',
      'categories' => ['featured'],
      'content' => file_get_contents($pattern_path),
    ]);
  }
});

require_once get_template_directory() . '/inc/setup.php';
