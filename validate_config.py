"""Validate public Galaxy configuration before deployment; no credentials needed."""
import json,re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
j=json.loads(Path(__file__).with_name('config_galaxy.json').read_text())
assert j['schema_version']==1 and j['application_id']=='com.luma.smartremote'
assert j['platform']=='android' and j['store']=='galaxy_store'
assert type(j['revision']) is int and j['revision']>=1
assert 60<=j['cache_ttl_seconds']<=86400
v=j['android']['galaxy_store']
assert 1<=v['min_supported_version_code']<=v['latest_version_code']
assert v['update_mode'] in ['none','soft','force']
assert v['update_url']=='https://galaxystore.samsung.com/detail/com.luma.smartremote'
assert j['ads']['app_id']=='ca-app-pub-3289974964220873~6139840770'
a=j['ads'];assert 300<=a['fullscreen_interval_seconds']<=3600 and 600<=a['app_open_interval_seconds']<=7200
assert set(a['placements'])=={'banner','native','interstitial','rewarded','rewarded_interstitial','app_open'}
ids=[]
for p in a['placements'].values():
 assert type(p['enabled']) is bool
 unit=p['unit_id'];assert unit=='' or re.fullmatch(r'ca-app-pub-3289974964220873/[0-9]{10}',unit)
 if unit:ids.append(unit)
 if a['enabled'] and p['enabled']:assert unit
assert len(ids)==len(set(ids))
for key in ['enabled','test_enabled']:assert type(a[key]) is bool
for key in ['reward_offer','pro_macros','pro_custom_remote','pro_widgets']:assert type(j['features'][key]) is bool
for value in j['kill_switches'].values():assert type(value) is bool
for key,value in j['links'].items():
 if key=='support_email':assert re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',value)
 else:
  u=urlsplit(value);assert u.scheme=='https' and u.hostname and not u.username and u.port in [None,443]
for name in ['privacy.html','terms.html']:
 text=Path(__file__).with_name(name).read_text();assert 'chennoufo11@gmail.com' in text and '<script' not in text
assert 'com.luma.smartremote' in Path(__file__).with_name('privacy.html').read_text()

class PublicPage(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=set();self.refs=[];self.scripts=[];self.current_script=None
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  assert not any(key.lower().startswith('on') for key in attrs), 'Inline event handlers are not allowed'
  if attrs.get('id'):
   assert attrs['id'] not in self.ids, 'Duplicate page ID'
   self.ids.add(attrs['id'])
  for key in ['href','src']:
   if attrs.get(key):self.refs.append(attrs[key])
  if tag=='script':
   self.current_script={'attrs':attrs,'body':''};self.scripts.append(self.current_script)
 def handle_data(self,data):
  if self.current_script is not None:self.current_script['body']+=data
 def handle_endtag(self,tag):
  if tag=='script':self.current_script=None

root=Path(__file__).parent
pages={}
for name in ['index.html','privacy.html','terms.html']:
 text=(root/name).read_text();assert 'chennoufo11@gmail.com' in text
 page=PublicPage();page.feed(text);pages[name]=page
for name,page in pages.items():
 for ref in page.refs:
  url=urlsplit(ref)
  assert url.scheme in ['', 'https', 'mailto'], 'Unsupported link scheme'
  if not url.scheme and not url.netloc:
   target=url.path or name
   assert (root/target).resolve().is_relative_to(root.resolve()), 'Asset outside public site'
   assert (root/target).is_file(), f'Missing local asset: {target}'
   if url.fragment:assert target in pages and url.fragment in pages[target].ids, 'Missing anchor'
scripts=pages['index.html'].scripts
assert len(scripts)==2
assert scripts[0]['attrs']=={'defer':None,'src':'site.js'} and not scripts[0]['body'].strip()
assert scripts[1]['attrs']=={'type':'application/ld+json'}
structured=json.loads(scripts[1]['body'])
assert structured['@type']=='SoftwareApplication' and structured['name']=='Smart TV Remote Control'
assert structured['url']=='https://metosapps.github.io/LumaRemoteGalaxyConfig/'
print('Galaxy config, public policies and landing-page assets validated.')
