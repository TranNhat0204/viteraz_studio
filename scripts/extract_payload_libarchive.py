import ctypes as c
from pathlib import Path
l=c.CDLL('libarchive.so.13')
def fn(n,args,ret):
 f=getattr(l,n);f.argtypes=args;f.restype=ret;return f
ptr=c.c_void_p
new=fn('archive_read_new',[],ptr);support=fn('archive_read_support_format_all',[ptr],c.c_int);filters=fn('archive_read_support_filter_all',[ptr],c.c_int);op=fn('archive_read_open_filename',[ptr,c.c_char_p,c.c_size_t],c.c_int);nxt=fn('archive_read_next_header',[ptr,c.POINTER(ptr)],c.c_int);name=fn('archive_entry_pathname',[ptr],c.c_char_p);read=fn('archive_read_data',[ptr,ptr,c.c_size_t],c.c_ssize_t);err=fn('archive_error_string',[ptr],c.c_char_p)
a=new();support(a);filters(a);print('open',op(a,b'analysis/payload.7z',10240));e=ptr();root=Path('analysis/payload').resolve();root.mkdir(exist_ok=True);buf=c.create_string_buffer(1024*1024);count=0
while True:
 status=nxt(a,c.byref(e))
 if status==1:break
 if status<0:raise RuntimeError(err(a))
 rel=name(e).decode();p=(root/rel).resolve()
 if not p.is_relative_to(root):raise ValueError(rel)
 if rel.endswith('/'):
  p.mkdir(parents=True,exist_ok=True);continue
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('wb') as out:
  while True:
   n=read(a,buf,len(buf))
   if n<0:raise RuntimeError(err(a))
   if n==0:break
   out.write(buf.raw[:n])
 count+=1
 if count<15:print(rel)
print('files',count)
