# Genera el diagrama de arquitectura de Mu (SVG horizontal + vertical) dentro de la ventana emergente de mu_guia.html.
# Uso: python research/grafo/mu_guia_arq.py  (reemplaza el <figure class="arqf"> existente; identidad: .claude/skills/mu/IDENTIDAD.md)
import pathlib,re
def T(x,y,s,cls="t",anchor="start",size=None,weight=None,fill=None):
    a=f' text-anchor="{anchor}"' if anchor!="start" else ""
    st=[]
    if size: st.append(f"font-size:{size}px")
    if weight: st.append(f"font-weight:{weight}")
    if fill: st.append(f"fill:{fill}")
    stl=f' style="{";".join(st)}"' if st else ""
    return f'<text x="{x}" y="{y}" class="{cls}"{a}{stl}>{s}</text>'
def R(x,y,w,h,cls="inv",sw=2,extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}" stroke="currentColor" stroke-width="{sw}"{extra}/>'
def F(x,y,w,h,cls): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}"/>'
def L(x1,y1,x2,y2,sw=2,cls="",dash=False,mk=None):
    d=' stroke-dasharray="5 4"' if dash else ""
    m=f' marker-end="url(#{mk})"' if mk else ""
    c=f' class="{cls}"' if cls else ' stroke="currentColor"'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"{c} stroke-width="{sw}"{d}{m}/>'
def C(cx,cy,r,cls="inv",sw=2): return f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls}" stroke="currentColor" stroke-width="{sw}"/>'

# ---- ilustraciones (zona de 220x64 a partir de x,y) ----
def il_investigar(x,y):
    o=[]
    # papel
    o+= [R(x+8,y+4,34,44),L(x+15,y+16,x+35,y+16,1.5),L(x+15,y+24,x+35,y+24,1.5),L(x+15,y+32,x+29,y+32,1.5),T(x+25,y+62,"papers","t s","middle")]
    # globo de diálogo
    o+= [f'<path d="M{x+88} {y+6} h40 v28 h-24 l-8 10 v-10 h-8 z" class="inv" stroke="currentColor" stroke-width="2"/>',T(x+108,y+62,"redes","t s","middle")]
    # barras negocio
    o+= [F(x+164,y+30,9,18,"fg"),F(x+177,y+20,9,28,"fg"),F(x+190,y+8,9,40,"fg"),L(x+160,y+48,x+204,y+48,2),T(x+182,y+62,"negocio","t s","middle")]
    return "".join(o)
def il_registro(x,y):
    o=[R(x+10,y+2,200,58,"inv",2)]
    rows=[("F-1","Arrow 1963","A"),("F-16","Mertens 2022","A"),("F-506","Gestión 2026","C"),("F-542","Salvi 2025","A")]
    for i,(f,a,r) in enumerate(rows):
        yy=y+2+i*14.5
        if i: o.append(L(x+10,yy,x+210,yy,1))
        o.append(T(x+16,yy+11,f,"t s b"))
        o.append(T(x+62,yy+11,a,"t s"))
        o.append(F(x+186,yy+2,18,11,"acc" if r=="C" else "fg"))
        o.append(T(x+195,yy+11,r,"t s b" ,"middle",fill="#000" if r=="C" else None) if r=="C" else T(x+195,yy+11,r,"t s b inv","middle"))
    return "".join(o)
def il_nodes(x,y):
    o=[C(x+110,y+30,15,"fg",2),T(x+110,y+34,"alma","t s b inv","middle")]
    pos=[(x+20,y+6),(x+20,y+38),(x+176,y+6),(x+176,y+38)]
    for px,py in pos:
        cx,cy=px+12,py+10
        o.insert(0,L(cx,cy,x+110,y+30,1.5))
        o+= [R(px,py,24,20,"inv",2),L(px+5,py+7,px+19,py+7,1),L(px+5,py+13,px+15,py+13,1)]
    o.append(T(x+110,y+62,"16 nodes · 1 mapa","t s","middle"))
    return "".join(o)
def il_grafo(x,y):
    P=[(x+30,y+14),(x+70,y+40),(x+112,y+10),(x+150,y+42),(x+190,y+16),(x+108,y+50)]
    E=[(0,1),(1,2),(2,3),(3,4),(1,5),(5,3),(0,2)]
    o=[L(*P[a],*P[b],1.5) for a,b in E]
    o.append(L(*P[2],*P[4],2.5,"stk-acc",True))
    o+=[C(px,py,6,"fg",0) for px,py in P]
    o.append(T(x+150,y+8,"choque","t s","middle",fill="var(--acc)",weight=700))
    o.append(T(x+110,y+66,"entidades · relaciones","t s","middle"))
    return "".join(o)
def il_panel(x,y):
    o=[T(x+10,y+40,"Nx","t",size=38,weight=900),T(x+60,y+40,"/7","t s")]
    for i,h in enumerate([40,30,46,22]):
        o.append(F(x+120+i*22,y+48-h,14,h,"acc" if i==3 else "fg"))
    o.append(L(x+114,y+48,x+212,y+48,2))
    o.append(T(x+110,y+62,"salud · madurez · riqueza","t s","middle"))
    return "".join(o)
def il_auditoria(x,y):
    o=[]
    for i,cls in enumerate(["fg","g2","acc"]):
        o.append(C(x+70+i*40,y+22,13,cls,2))
    o.append(T(x+110,y+56,"3 preguntas · semáforos","t s","middle"))
    return "".join(o)
CARDS=[(1,"INVESTIGAR","/trinidad","papers, redes, negocio",il_investigar,False),
       (2,"REGISTRO","/cronista","fuentes/codice.md",il_registro,False),
       (3,"NODES","/many-brains","_nodes/ + alma.md",il_nodes,False),
       (4,"GRAFO","/grafo","grafo/relaciones/",il_grafo,False),
       (5,"PANEL","/mu","grafo/mu.html",il_panel,False),
       (6,"AUDITORÍA","/chacal","research/garaje/",il_auditoria,True)]
W,Hc=240,150
def card(x,y,n,title,cmd,file,il,hot):
    o=[R(x,y,W,Hc,"inv",4 if hot else 2)]
    o.append(F(x,y,34,34,"acc" if hot else "fg"))
    o.append(T(x+17,y+25,str(n),"t" if hot else "t inv","middle",size=20,weight=900,fill="#000" if hot else None))
    o.append(T(x+44,y+22,title,"t b",size=14))
    cw=len(cmd)*7.4+10
    o.append(F(x+W-cw-8,y+9,cw,18,"fg"));o.append(T(x+W-8-cw/2,y+22,cmd,"t s b inv","middle"))
    o.append(il(x+10,y+44))
    o.append(T(x+10,y+Hc-8,file,"t s",fill="var(--g2)"))
    return "".join(o)
def lab(x,y,s,anchor="middle",acc=False):
    w=len(s)*6.2+10
    x0=x-w/2 if anchor=="middle" else (x if anchor=="start" else x-w)
    return F(x0,y-11,w,15,"inv")+T(x0+w/2,y,s,"t s","middle",fill="var(--acc)" if acc else None,weight=700 if acc else None)
def defs(sfx):
    return (f'<defs><marker id="ah{sfx}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="currentColor"/></marker>'
            f'<marker id="ao{sfx}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="acc"/></marker></defs>')
ARIA="Arquitectura de Mu: investigar anota fuentes en el registro, el registro se cita en los nodes, registro y nodes se leen de a cinco para el grafo, el grafo se cuenta en el panel, el panel se audita, y la auditoría abre tareas de corrección que vuelven a investigar."
def wide():
    VW,VH=960,560
    xs=[40,360,680]; y1,y2=70,330
    pos={1:(xs[0],y1),2:(xs[1],y1),3:(xs[2],y1),4:(xs[2],y2),5:(xs[1],y2),6:(xs[0],y2)}
    o=[f'<svg viewBox="0 0 {VW} {VH}" role="img" aria-label="{ARIA}" class="arq-w">',defs("w")]
    o.append(T(40,40,"CÓMO FLUYE EL CONOCIMIENTO","t b",size=13))
    # flechas
    cy1=y1+Hc/2; cy2=y2+Hc/2
    o.append(L(xs[0]+W,cy1,xs[1]-4,cy1,3,mk="ahw"));o.append(lab((xs[0]+W+xs[1])/2,cy1-10,"anota F-n"))
    o.append(L(xs[1]+W,cy1,xs[2]-4,cy1,3,mk="ahw"));o.append(lab((xs[1]+W+xs[2])/2,cy1-10,"se cita en"))
    o.append(L(xs[2]+W/2,y1+Hc,xs[2]+W/2,y2-4,3,mk="ahw"));o.append(lab(xs[2]+W/2,(y1+Hc+y2)/2+4,"se lee de a 5"))
    o.append(L(xs[2],cy2,xs[1]+W+4,cy2,3,mk="ahw"));o.append(lab((xs[1]+W+xs[2])/2,cy2-10,"se cuenta"))
    o.append(L(xs[1],cy2,xs[0]+W+4,cy2,3,mk="ahw"));o.append(lab((xs[0]+W+xs[1])/2,cy2-10,"se audita"))
    # registro también alimenta al grafo (diagonal punteada)
    o.append(L(xs[1]+W-30,y1+Hc,xs[2]+30,y2-4,2,dash=True,mk="ahw"));o.append(lab(xs[1]+W+40,(y1+Hc+y2)/2+34,"fuentes"))
    # bucle de corrección: de 6 sube a 1 por la izquierda
    o.append(f'<path d="M{xs[0]+40} {y2} V{y1+Hc+4}" class="stk-acc" stroke-width="4" fill="none" marker-end="url(#aow)"/>')
    o.append(lab(xs[0]+40,(y1+Hc+y2)/2+4,"corrige y vuelve a probar",acc=True))
    for n,t,c,f,il,h in CARDS: o.append(card(*pos[n],n,t,c,f,il,h))
    # banda inferior
    yb=y2+Hc+30
    o.append(L(40,yb,920,yb,2,dash=True))
    o.append(T(40,yb+20,"LEEN EL REGISTRO: El Lobo · /cerrajero · /lapuerta","t s"))
    o.append(T(920,yb+20,"PUBLICAR: /actualizar → main","t s b","end"))
    o.append('</svg>')
    return "".join(o)
def tall():
    VW=360; gap=70; x=60; y0=40
    ys=[y0+i*(Hc+gap) for i in range(6)]
    VH=ys[-1]+Hc+70
    o=[f'<svg viewBox="0 0 {VW} {VH}" role="img" aria-label="{ARIA}" class="arq-t">',defs("t")]
    o.append(T(10,24,"CÓMO FLUYE EL CONOCIMIENTO","t b",size=13))
    labels=["anota F-n","se cita en","se lee de a 5","se cuenta","se audita"]
    for i in range(5):
        cx=x+W/2
        o.append(L(cx,ys[i]+Hc,cx,ys[i+1]-4,3,mk="aht"));o.append(lab(cx,(ys[i]+Hc+ys[i+1])/2+5,labels[i]))
    # bucle por la izquierda
    lx=28
    o.append(f'<path d="M{x} {ys[5]+Hc/2} H{lx} V{ys[0]+Hc/2} H{x-4}" class="stk-acc" stroke-width="4" fill="none" marker-end="url(#aot)"/>')
    mid=(ys[0]+ys[5])/2+Hc/2
    o.append(f'<text x="{lx-8}" y="{mid}" class="t s" text-anchor="middle" transform="rotate(-90 {lx-8} {mid})" style="fill:var(--acc);font-weight:700">↑ corrige y vuelve a probar</text>')
    for i,(n,t,c,f,il,h) in enumerate(CARDS): o.append(card(x,ys[i],n,t,c,f,il,h))
    yb=ys[-1]+Hc+26
    o.append(T(10,yb,"LEEN EL REGISTRO: Lobo · /cerrajero · /lapuerta","t s"))
    o.append(T(10,yb+18,"PUBLICAR: /actualizar → main","t s b"))
    o.append('</svg>')
    return "".join(o)
g=pathlib.Path(__file__).resolve().parent / 'mu_guia.html';s=g.read_text()
fig=('<figure class="arqf">'+wide()+tall()+
 '<figcaption>Las seis capas de Mu y lo que pasa entre ellas. Lo investigado se anota en el registro, se cita en los nodes y se lee de a cinco fuentes para armar el grafo. El panel cuenta todo con reglas fijas y el auditor mide qué evidencia hay detrás. Lo que falla vuelve, en naranja, como tarea de corrección. El panel y el auditor nunca editan nodes ni registro.</figcaption></figure>')
a=s.index('<figure class="arqf">'); b=s.index('</figure>',a)+9
s=s[:a]+fig+s[b:]
css='''
.arqf{margin:0;padding:12px 16px 14px}.arqf svg{color:var(--fg);width:100%;height:auto;display:block}
.arqf .arq-t{display:none}@media(max-width:720px){.arqf .arq-w{display:none}.arqf .arq-t{display:block}}
.arqf figcaption{font-size:11px;color:var(--g2);border-top:2px solid var(--fg);margin-top:8px;padding-top:6px}
.stk-acc{stroke:var(--acc)}
'''
g.write_text(s)
print('ok')
