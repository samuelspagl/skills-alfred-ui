#!/usr/bin/env python3
"""Validate reference-package integrity, without launching Alfred or running actions."""
import json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
errors=[];json_count=0;link_count=0
for p in root.rglob('*.json'):
 try:json.loads(p.read_text());json_count+=1
 except Exception as e:errors.append(f'{p.relative_to(root)}: {e}')
for p in root.rglob('*.md'):
 for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
  target=match.group(1).split('#')[0]
  if not target or re.match(r'^[a-z]+:',target):continue
  link_count+=1
  if not (p.parent/target).exists():errors.append(f'{p.relative_to(root)}: missing {target}')
packages=list((root/'examples').glob('*.alfredui'))
for package in packages:
 d=json.loads((package/'ui.json').read_text());ids=[]
 def walk(x):
  if isinstance(x,list):
   for v in x:walk(v)
  elif isinstance(x,dict):
   if isinstance(x.get('id'),str) and 'type' in x:ids.append(x['id'])
   if x.get('type')=='script' and isinstance(x.get('src'),str) and not (package/x['src']).is_file():errors.append(f'{package.name}: missing script {x["src"]}')
   for v in x.values():walk(v)
 walk(d)
 if len(ids)!=len(set(ids)):errors.append(f'{package.name}: duplicate literal component ids')
 if 'pulse' in d and not (package/d['pulse']['src']).is_file():errors.append(f'{package.name}: missing pulse script')
 if not isinstance(d.get('window',{}).get('root'),dict):errors.append(f'{package.name}: missing window.root')
print(f'JSON files parsed: {json_count}; local Markdown links checked: {link_count}; example packages: {len(packages)}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('Package integrity checks passed. Alfred runtime behavior was not tested.')
