"""Build an isolated classic WP theme from the preserved non-blog capture."""
from pathlib import Path
from bs4 import BeautifulSoup
import shutil,json,zipfile,re
from urllib.parse import urlparse,unquote,urljoin
root=Path(__file__).parent
src=root/'dist'; out=root/'wordpress-build-v2'/'fuhyo-reproduction'
out.mkdir(parents=True,exist_ok=True)
dependencies=set(); missing=set()
def asset(url,base='/'):
    if url.startswith('data:'):return
    url=urljoin(base,url)
    parsed=urlparse(url)
    if parsed.netloc and parsed.netloc!='net-fuhyohigai-taisaku.co.jp':return
    path=unquote(parsed.path).lstrip('/')
    if not path or path in dependencies:return
    f=src/path
    if not f.is_file():
        missing.add(path);return
    dependencies.add(path)
    target=out/'static'/path;target.parent.mkdir(parents=True,exist_ok=True)
    if f.suffix=='.css':
        css=f.read_text()
        def repl(m):
            u=m.group(1).strip(' \"\'')
            if u.startswith('data:'):return m.group(0)
            asset(u,'/'+path)
            p=urlparse(urljoin('/'+path,u))
            if not p.netloc or p.netloc=='net-fuhyohigai-taisaku.co.jp':
                import posixpath
                return 'url("'+posixpath.relpath(unquote(p.path).lstrip('/'),str(Path(path).parent))+'")'
            return m.group(0)
        target.write_text(re.sub(r'url\(([^)]+)\)',repl,css))
    else:shutil.copy2(f,target)
(out/'pages').mkdir(exist_ok=True)
routes={}
for f in [src/'index.html',*sorted((src/'top').rglob('index.html')),src/'thanks/index.html']:
    route='/' + str(f.relative_to(src).parent).replace('.','').strip('/')
    route=route.rstrip('/')+'/'
    soup=BeautifulSoup(f.read_text(),'html.parser')
    for tag in soup.select('script, form, link[rel="canonical"], meta[property="og:url"], link[rel="alternate"], link[rel="https://api.w.org/"]'): tag.decompose()
    for tag in soup.find_all(True):
        for key in ['src','href','poster']:
            u=tag.get(key,'')
            if any(x in u for x in ['/wp-content/','/wp-includes/','/assets/']):asset(u)
        for u in tag.get('srcset','').split(','):
            if u.strip():asset(u.strip().split()[0])
        for u in re.findall(r'url\(([^)]+)\)',tag.get('style','')):asset(u.strip(' \"\''))
    for t in soup.select('style'):
        for u in re.findall(r'url\(([^)]+)\)',t.get_text()):asset(u.strip(' \"\''))
    for a in soup.select('a[href]'):
        if a['href'].startswith(('/column/','/column-category/')):a['href']='https://net-fuhyohigai-taisaku.co.jp'+a['href']
    for tag in soup.select('.elementor-invisible'):tag['class']=[c for c in tag['class'] if c!='elementor-invisible']
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.startswith('on'): del tag[attr]
    name=str(len(routes))+'.html'; routes[route]=name
    (out/'pages'/name).write_text(str(soup))
(out/'routes.json').write_text(json.dumps(routes,ensure_ascii=False,indent=2))
(out/'style.css').write_text('/*\nTheme Name: Fuhyo Reproduction\nVersion: 0.3.0\nRequires PHP: 8.1\nDescription: Non-blog captured layout, independent of Elementor plugin.\n*/')
(out/'functions.php').write_text('''<?php
defined('ABSPATH') || exit;
add_action('after_setup_theme',function(){add_theme_support('title-tag');});
add_action('template_redirect',function(){
 $routes=json_decode(file_get_contents(__DIR__.'/routes.json'),true);
 $path=rawurldecode(parse_url($_SERVER['REQUEST_URI'],PHP_URL_PATH));
 $base=parse_url(home_url('/'),PHP_URL_PATH);
 if($base && strpos($path,$base)===0) $path='/'.substr($path,strlen($base));
 $path='/'.trim($path,'/').'/'; if($path==='//')$path='/';
 if(!isset($routes[$path]))return;
 status_header(200);
 $html=file_get_contents(__DIR__.'/pages/'.$routes[$path]);
 $asset=esc_url(get_template_directory_uri().'/static');
 $html=preg_replace('~(?:https://net-fuhyohigai-taisaku.co.jp)?/(wp-content|wp-includes|assets)/~',$asset.'/$1/',$html);
 $html=str_replace('"/scroll-fix.css"','"'.esc_url(get_template_directory_uri().'/runtime.css').'"',$html);
 foreach(array_keys($routes) as $route){$html=str_replace('href="'.$route.'"','href="'.esc_url(home_url($route)).'"',$html);}
 $html=str_replace('</head>','<link rel="stylesheet" href="'.esc_url(get_template_directory_uri().'/runtime.css').'" /></head>',$html);
 $html=str_replace('</body>','<script src="'.esc_url(get_template_directory_uri().'/runtime.js').'" defer></script></body>',$html);
 ob_start();wp_head();$head=ob_get_clean();
 ob_start();wp_footer();$foot=ob_get_clean();
 $html=str_replace('</head>',$head.'</head>',$html);
 $html=str_replace('</body>',$foot.'</body>',$html);
 echo $html;exit;
});
''')
(out/'index.php').write_text('<?php get_header(); while(have_posts()){the_post();the_title("<h1>","</h1>");the_content();} get_footer();')
(out/'header.php').write_text('<!doctype html><html <?php language_attributes(); ?>><head><meta charset="<?php bloginfo("charset"); ?>"><meta name="viewport" content="width=device-width,initial-scale=1"><?php wp_head(); ?></head><body <?php body_class(); ?>><?php wp_body_open(); ?>')
(out/'footer.php').write_text('<?php wp_footer(); ?></body></html>')
(out/'runtime.css').write_text((src/'scroll-fix.css').read_text()+'''\nhtml{scroll-behavior:smooth}img{max-width:100%}.jkit-menu-wrapper.is-open{display:block!important;visibility:visible!important;transform:none!important;opacity:1!important;left:0!important}.jkit-menu-overlay.is-open{display:block!important;opacity:1!important;visibility:visible!important}.menu-item-has-children:focus-within>.sub-menu{visibility:visible!important;opacity:1!important;display:block!important}.testimonials-track,.client-list{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}.testimonial-item{flex:0 0 100%;scroll-snap-align:start}.client-slider{flex:0 0 20%;scroll-snap-align:start}@media(max-width:767px){.client-slider{flex-basis:50%}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}''')
(out/'runtime.js').write_text('''document.addEventListener('DOMContentLoaded',()=>{
document.querySelectorAll('.jkit-accordion .card-wrapper').forEach(c=>c.querySelector('a')?.setAttribute('aria-expanded',String(c.classList.contains('expand'))));
document.addEventListener('click',e=>{const b=e.target.closest('.jkit-hamburger-menu,.jkit-close-menu,.jkit-menu-overlay');if(b){const n=b.closest('.jkit-nav-menu');const m=n?.querySelector('.jkit-menu-wrapper');if(m){const open=!m.classList.contains('is-open');m.classList.toggle('is-open',open);n.querySelector('.jkit-menu-overlay')?.classList.toggle('is-open',open);n.querySelector('.jkit-hamburger-menu')?.setAttribute('aria-expanded',String(open));}}
const h=e.target.closest('.jkit-accordion .card-header');if(h){e.preventDefault();const card=h.closest('.card-wrapper'),open=!card.classList.contains('expand');h.closest('.jkit-accordion').querySelectorAll('.card-wrapper').forEach(c=>{const active=c===card&&open;c.classList.toggle('expand',active);c.querySelector('.card-expand').style.display=active?'block':'none';c.querySelector('a').setAttribute('aria-expanded',String(active));});}});
document.addEventListener('keydown',e=>{if(e.key==='Escape')document.querySelectorAll('.is-open').forEach(n=>n.classList.remove('is-open'));});
document.querySelectorAll('.testimonials-track,.client-list').forEach(track=>{if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;let paused=false;track.addEventListener('mouseenter',()=>paused=true);track.addEventListener('mouseleave',()=>paused=false);track.addEventListener('focusin',()=>paused=true);track.addEventListener('focusout',()=>paused=false);setInterval(()=>{if(paused||document.hidden)return;const width=track.firstElementChild?.getBoundingClientRect().width||track.clientWidth;track.scrollTo({left:track.scrollLeft+track.clientWidth>=track.scrollWidth-5?0:track.scrollLeft+width,behavior:'smooth'});},3500);});
});''')
with zipfile.ZipFile(root/'wordpress-build-v2'/'fuhyo-reproduction.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in out.rglob('*'):
        if f.is_file():z.write(f,f.relative_to(out.parent))
report={'routes':routes,'assets':len(dependencies),'missing':sorted(missing),'zip_bytes':(out.parent/'fuhyo-reproduction.zip').stat().st_size}
(out.parent/'build-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))
