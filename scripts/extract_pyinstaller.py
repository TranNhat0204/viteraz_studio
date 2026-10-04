from pathlib import Path
import struct,zlib,marshal,types,dis,json,importlib.util
p=Path('analysis/payload/resources/backend/backend.exe').read_bytes();cookie=p.rfind(b'MEI\014\013\012\013\016');magic,total,tocpos,toclen,ver,lib=struct.unpack('!8sIIII64s',p[cookie:cookie+88]);start=cookie+88-total;pos=start+tocpos;end=pos+toclen;root=Path('Tools/RevoStudio/recovered/backend');root.mkdir(parents=True,exist_ok=True);entries=[]
while pos<end:
 size,off,clen,ulen,flag,typ=struct.unpack('!IIIIBc',p[pos:pos+18]);name=p[pos+18:pos+size].split(b'\0')[0].decode();raw=p[start+off:start+off+clen];raw=zlib.decompress(raw) if flag else raw;dest=root/'archive'/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw);entries.append({'name':name,'type':typ.decode(),'size':len(raw)});pos+=size
(root/'archive-index.json').write_text(json.dumps(entries,indent=2));print('archive entries',len(entries));print(entries[:12])
pyz=root/'archive/PYZ.pyz'
if not pyz.exists():pyz=next((root/'archive').glob('PYZ*'))
b=pyz.read_bytes();off=struct.unpack('!I',b[8:12])[0];toc=marshal.loads(b[off:]);toc=dict(toc);mods=[]
for name,(typ,pos,size) in toc.items():
 
 if size==0:continue
 raw=zlib.decompress(b[pos:pos+size]);dest=root/'bytecode'/Path(*name.split('.'));dest=dest.with_suffix('.pyc');dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b[4:8]+b'\0'*12+raw);mods.append(name)
(root/'modules.json').write_text(json.dumps(mods,indent=2));print('modules',len(mods));print('\n'.join(x for x in mods if x.startswith(('app','backend','revo','src'))))
