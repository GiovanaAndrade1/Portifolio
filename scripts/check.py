from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
class Check(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.h1=0
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='h1':self.h1+=1
  for k in ('href','src'):
   if k in d:self.refs.append(d[k])
root=Path(__file__).resolve().parents[1];errors=[];pages=list(root.rglob('*.html'))
for f in pages:
 p=Check();p.feed(f.read_text(encoding='utf-8'))
 if p.h1!=1:errors.append(f'{f.name}: {p.h1} h1')
 for ref in p.refs:
  url=urlsplit(ref)
  if url.scheme or not url.path:continue
  target=(f.parent/unquote(url.path)).resolve()
  if not target.exists():errors.append(f'{f.name}: ausente {ref}')
print(f'{len(pages)} páginas verificadas; {len(errors)} erros de links/arquivos/títulos.')
for x in errors:print(x)
raise SystemExit(bool(errors))
