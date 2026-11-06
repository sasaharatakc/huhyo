import {spawn} from 'node:child_process';
import fs from 'node:fs';
const root='/workspace/scratch/b877ca8d2a01';
const p=spawn(process.execPath,[root+'/wp-runtime/node_modules/@wp-playground/cli/cli.js','server','--port=9403','--workers=1','--wordpress-install-mode=install-from-existing-files',`--mount-before-install=${root}/wp-core/wordpress:/wordpress`,`--mount=${root}/fuhyo-source/wordpress-build-v2/fuhyo-reproduction:/wordpress/wp-content/themes/fuhyo-reproduction`,`--blueprint=${root}/fuhyo-source/wp-test.json`],{stdio:['ignore','pipe','pipe']});
let started=false;const timer=setTimeout(()=>{console.error('Startup timeout');p.kill();process.exitCode=1},120000);
p.stdout.on('data',async b=>{if(started||!b.toString().includes('Ready!'))return;started=true;clearTimeout(timer);
try {const routes=JSON.parse(fs.readFileSync(root+'/fuhyo-source/wordpress-build-v2/fuhyo-reproduction/routes.json'));const results=[];
const assets=new Set();
for(const route of Object.keys(routes)){const r=await fetch('http://127.0.0.1:9403'+encodeURI(route));const html=await r.text();for(const m of html.matchAll(/(?:src|href)="(http:\/\/127\.0\.0\.1:9403\/wp-content\/themes\/[^"<>]+)"/g))assets.add(m[1].replaceAll('&amp;','&'));results.push({route,status:r.status,bytes:html.length,phpError:/Fatal error|Parse error|Warning:/.test(html),elementorJS:/<script[^>]+src=[^>]*elementor/.test(html)});}
const failures=[];for(const url of assets){const r=await fetch(url);if(r.status!==200)failures.push({url,status:r.status});await r.arrayBuffer();}
fs.writeFileSync(root+'/fuhyo-source/wordpress-build-v2/asset-test.json',JSON.stringify({checked:assets.size,failures},null,2));console.log(JSON.stringify({assets:assets.size,failures}));
if(failures.length||results.some(r=>r.status!==200||r.phpError||r.elementorJS))process.exitCode=1;
fs.writeFileSync(root+'/fuhyo-source/wordpress-build-v2/http-test.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results));
}catch(e){console.error(e);process.exitCode=1}finally{p.kill();}});
p.stderr.on('data',b=>process.stderr.write(b));

