import sys,json,marshal,types,dis,ast,shutil,hashlib
from pathlib import Path
import depyf,jsbeautifier,signal
def timeout_handler(*args): raise TimeoutError("decompilation exceeded 2 seconds")
signal.signal(signal.SIGALRM,timeout_handler)
root=Path('Tools/RevoStudio');report=root/'reports';report.mkdir(exist_ok=True)
app=root/'recovered/app';pretty=root/'readable/javascript';js=[]
for p in app.rglob('*.js'):
 if 'node_modules' in p.parts:continue
 out=pretty/p.relative_to(app);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(jsbeautifier.beautify(p.read_text()),encoding='utf-8');js.append(str(out.relative_to(root)))
backend=root/'recovered/backend';results=[];ok=0;fail=0
for p in sorted((backend/'bytecode').rglob('*.pyc')):
 rel=p.relative_to(backend/'bytecode')
 if rel.parts[0] not in ('app','app.pyc'):continue
 code=marshal.loads(p.read_bytes()[16:]);out=root/'readable/python-disassembly'/rel.with_suffix('.txt');out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w') as f:dis.dis(code,file=f)
 chunks=['# PARTIAL DECOMPILATION: isolated functions, not a runnable module.\n# Module: '+str(rel)+'\n# Original imports, classes, decorators and initialization are NOT reconstructed.\n']
 def walk(c):
  global ok,fail
  for child in c.co_consts:
   if not isinstance(child,types.CodeType):continue
   if child.co_name.isidentifier() and child.co_flags&2:
    try:
     signal.alarm(2);source=depyf.decompile(child);ast.parse(source);signal.alarm(0);chunks.append('\n# Original qualified name: '+child.co_qualname+'\n'+source+'\n');ok+=1;results.append({'module':str(rel),'name':child.co_qualname,'status':'decompiled_syntax_valid_semantics_unverified'})
    except Exception as e:
     signal.alarm(0)
     fail+=1;results.append({'module':str(rel),'name':child.co_qualname,'status':'not_decompiled','reason':type(e).__name__});chunks.append('\n# NOT DECOMPILED: '+child.co_qualname+'\n')
   walk(child)
 walk(code);out=root/'readable/python-partial'/rel.with_suffix('.py');out.parent.mkdir(parents=True,exist_ok=True);out.write_text('\n'.join(chunks))
(report/'decompilation.json').write_text(json.dumps(results,indent=2));(report/'summary.json').write_text(json.dumps({'javascript_formatted':len(js),'python_functions_syntax_valid':ok,'python_functions_failed':fail},indent=2));print('summary',len(js),ok,fail)
# Preserve shipped text resources, excluding dependencies; originals are never executed.
internal=Path('analysis/payload/resources/backend/_internal')
for name in ['app','alembic','crawlers','tts2']:
 src=internal/name
 if src.exists():shutil.copytree(src,root/'recovered/backend/shipped'/name,dirs_exist_ok=True)
for name in ['alembic.ini']:
 if (internal/name).exists():shutil.copy2(internal/name,root/'recovered/backend/shipped'/name)
ima=Path('analysis/payload/resources/ima2');dest=root/'recovered/ima2';dest.mkdir(exist_ok=True)
for name in ['package.json','package-lock.json']:shutil.copy2(ima/name,dest/name)
(report/'inputs.sha256').write_text('\n'.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name for p in [Path('upload/Revo.Studio.Setup.1.4.3.zip'),Path('analysis/Revo.Studio.Setup.1.4.3.exe'),Path('analysis/payload/resources/app.asar')])+'\n')
