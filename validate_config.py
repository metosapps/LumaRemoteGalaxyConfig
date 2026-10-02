"""Validate public Galaxy configuration before deployment; no credentials needed."""
import json,re
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
for value in j['kill_switches'].values():assert type(value) is bool
for key,value in j['links'].items():
 if key=='support_email':assert re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',value)
 else:
  u=urlsplit(value);assert u.scheme=='https' and u.hostname and not u.username and u.port in [None,443]
for name in ['privacy.html','terms.html','index.html']:
 text=Path(__file__).with_name(name).read_text();assert 'chennoufo11@gmail.com' in text and '<script' not in text
assert 'com.luma.smartremote' in Path(__file__).with_name('privacy.html').read_text()
print('Galaxy config and public policies validated.')
