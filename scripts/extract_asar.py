import json,struct,shutil
from pathlib import Path
p=Path('analysis/payload/resources/app.asar');d=p.read_bytes();print('asar',len(d),struct.unpack('<4I',d[:16]));h=json.loads(d[16:16+struct.unpack_from('<I',d,12)[0]]);base=8+struct.unpack_from('<I',d,4)[0];root=Path('Tools/RevoStudio/recovered/app').resolve();root.mkdir(parents=True,exist_ok=True);stats=[]
def walk(node,rel=Path()):
 for n,v in node['files'].items():
  r=rel/n;dest=(root/r).resolve()
  if not dest.is_relative_to(root):raise ValueError(r)
  if 'files' in v:walk(v,r)
  elif 'offset' in v:
   off=base+int(v['offset']);size=v['size'];assert off+size<=len(d);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(d[off:off+size]);stats.append(str(r))
  elif v.get('unpacked'):
   src=Path(str(p)+'.unpacked')/r
   if src.exists():dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
   else:print('missing unpacked',r)
walk(h);print('extracted',len(stats));print('\n'.join(stats[:40]))
