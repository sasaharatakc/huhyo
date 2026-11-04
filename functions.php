<?php
if (!defined('ABSPATH')) exit;
add_action('after_setup_theme', function () {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
  add_theme_support('html5', ['search-form','comment-form','comment-list','gallery','caption','style','script']);
  register_nav_menus(['primary'=>'Primary Navigation']);
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