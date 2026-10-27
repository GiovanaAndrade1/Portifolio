from pathlib import Path
from html import escape
import json,re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content/site.json').read_text(encoding='utf-8'))
NAV = [('index.html', 'Home', '⌂'), ('sobre.html', 'Sobre mim', '○'), ('projetos.html', 'Projetos', '▦'), ('stack.html', 'Stack', '◈'), ('contato.html', 'Contato', '↗')]

def e(value):
    return escape(str(value), quote=True)

def button(label, href):
    return f'<a class="button" href="{e(href)}">{e(label)} <span aria-hidden="true">→</span></a>'

def blocks(items):
    result = []
    for item in items:
        tag = item['tag']
        if tag not in ('h1','h2','h3','h4','p'): continue
        if tag == 'h3' or re.match(r'^\d{2}\s[—–]', item['text']): tag = 'h2'
        result.append(f'<{tag}>{e(item["text"])}</{tag}>')
    return '\n'.join(result)

def cards(projects, prefix=''):
    return '<div class="project-grid">' + ''.join(f'''
    <a class="project-card" href="{prefix}projetos/{p['slug']}.html">
      <div class="project-image"><img src="{prefix}assets/images/{p['image']}" alt="{e(p['title'])}" loading="lazy" width="800" height="480"><span class="project-arrow" aria-hidden="true">↗</span></div>
      <div class="project-info"><span class="eyebrow">{e(p['category'])}</span><h3>{e(p['title'])}</h3></div>
    </a>''' for p in projects) + '</div>'

def stack_cards(items, detailed=False):
    return '<div class="stack-grid">' + ''.join(f'''<article class="stack-card"><div class="stack-heading"><span class="tech-icon" aria-hidden="true"><img src="assets/icons/{e(t['icon'])}" alt="" width="44" height="44" loading="lazy"></span><div><h{2 if detailed else 3}>{e(t['name'])}</h{2 if detailed else 3}><span class="muted">{e(t['subtitle'])}</span></div></div>{f'<p>{e(t["description"])}</p>' if detailed else ''}</article>''' for t in items) + '</div>'

def page(filename, title, body, active='index.html', prefix=''):
    nav = ''.join(f'<a href="{prefix}{url}" {"aria-current=\"page\"" if active == url else ""}><span aria-hidden="true">{icon}</span>{label}</a>' for url,label,icon in NAV)
    social = f'<a href="{DATA["github"]}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to={DATA["email"]}" target="_blank" rel="noopener noreferrer">E-mail ↗</a><a href="{DATA["linkedin"]}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>'
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(DATA['intro'])}">
  <meta name="theme-color" content="#ffffff">
  <title>{e(title)} | {e(DATA['name'])}</title>
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}assets/css/styles.css">
  <script src="{prefix}assets/js/main.js" defer></script>
  <noscript><style>.navigation-panel {{ display: flex; }} .menu-toggle {{ display: none; }}</style></noscript>
</head>
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
  <div class="site-shell">
    <header class="sidebar">
      <a class="identity" href="{prefix}index.html"><img src="{prefix}assets/images/giovana.jpeg" alt="" width="48" height="48"><span><strong>{e(DATA['name'])}</strong><span>{e(DATA['role'])}</span></span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="navegacao"><span aria-hidden="true">☰</span><span class="sr-only">Abrir menu</span></button>
      <div class="navigation-panel" id="navegacao"><nav aria-label="Navegação principal">{nav}</nav><div class="social-links" aria-label="Redes sociais">{social}</div></div>
    </header>
    <div class="main-column">
      <main id="conteudo">{body}</main>
      <footer><span>© {DATA['name']}. Todos os direitos reservados.</span><div><a href="{prefix}privacidade.html">Privacidade</a><a href="{prefix}cookies.html">Cookies</a></div></footer>
    </div>
  </div>
</body>
</html>'''
    path = ROOT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')

STATUS = '<span class="availability"><span aria-hidden="true"></span>Available for Work</span>'

def intro(title, description=''):
    return f'<section class="intro">{STATUS}<h1>{e(title)}</h1>{f"<p>{e(description)}</p>" if description else ""}</section>'

def build():
    page('index.html', 'Portfólio', intro('Muito Prazer, me chamo Giovana Andrade...', DATA['intro']) + button('Mais sobre mim','sobre.html') + '<section class="section"><h2>Projetos Recentes</h2>' + cards(DATA['projects'][:3]) + button('Todos os projetos','projetos.html') + '</section><section class="section"><h2>Minha stack</h2>' + stack_cards(DATA['stack'][:3]) + button('Todas stacks','stack.html') + '</section>')
    page('projetos.html','Projetos',intro('Meus Projetos:') + cards(DATA['projects']), 'projetos.html')
    about = DATA['about']
    experiences = '<section class="prose"><h2>Experiências</h2>' + ''.join(f'<article class="experience"><h3>{e(x["title"])}</h3><div class="experience-meta"><span>{e(x["organization"])}</span><span>{e(x["period"])}</span></div><p>{e(x["description"])}</p></article>' for x in DATA['experiences']) + '</section>'
    page('sobre.html','Sobre mim', intro(about[0]['text'],about[1]['text']) + '<div class="prose">' + blocks(about[2:]) + '</div>' + experiences + button('Se interessou?','contato.html'),'sobre.html')
    page('stack.html','Minha stack',intro('Minhas Skills Stacks:') + stack_cards(DATA['stack'],True),'stack.html')
    contact = intro('Vamos conversar!','Sinta-se à vontade para entrar em contato caso tenha interesse no meu perfil ou alguma oportunidade profissional. Responderei o mais breve possível.') + f'''
    <section class="section contact-section"><h2>Entre em contato</h2>
      <form id="contact-form" data-email="{e(DATA['email'])}">
        <label for="nome">Nome</label><input id="nome" name="nome" autocomplete="name" required maxlength="120" placeholder="Seu nome">
        <label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="200" placeholder="seu@email.com">
        <label for="mensagem">Mensagem</label><textarea id="mensagem" name="mensagem" rows="6" required maxlength="5000" placeholder="Como podemos trabalhar juntos?"></textarea>
        <p class="form-hint">Abre o Gmail no navegador com a mensagem preenchida. Entre na sua conta, se necessário, revise e clique em Enviar.</p>
        <button class="button" type="submit">Abrir no Gmail <span aria-hidden="true">↗</span></button><p id="form-status" role="status" aria-live="polite"></p>
        <noscript><p>Escreva diretamente para <a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to={e(DATA['email'])}" target="_blank" rel="noopener noreferrer">{e(DATA['email'])}</a>.</p></noscript>
      </form>
    </section><section class="section"><h2>Contato</h2><a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to={e(DATA['email'])}" target="_blank" rel="noopener noreferrer">{e(DATA['email'])}</a><h2 class="social-title">Social</h2><div class="contact-social"><a href="{e(DATA['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="{e(DATA['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></section>'''
    page('contato.html','Contato',contact,'contato.html')
    for project in DATA['projects']:
        href = project['url']
        cta = f'<a class="button" href="{e(href)}" target="_blank" rel="noopener noreferrer">Visualizar projeto <span aria-hidden="true">↗</span></a>' if href else button('Conversar sobre o projeto','../contato.html')
        body = '<a class="back-link" href="../projetos.html">← Voltar</a>' + f'<section class="intro project-intro"><h1>{e(project["title"])}</h1><span class="eyebrow">{e(project["category"])}</span></section>' + cta + f'<img class="detail-image" src="../assets/images/{project["image"]}" alt="{e(project["title"])}" width="1000" height="600"><article class="prose">{blocks(project["body"])}</article><section class="section"><h2>Outros projetos</h2>' + cards([p for p in DATA['projects'] if p!=project][:2],'../') + '</section>'
        page(f'projetos/{project["slug"]}.html',project['title'],body,'projetos.html','../')
    page('privacidade.html','Privacidade',intro('Privacidade') + '<div class="prose"><p>Este portfólio estático não possui cadastro, ferramentas de análise de acesso ou armazenamento de dados pessoais no navegador.</p><p>O formulário abre o Gmail no navegador com os dados informados na mensagem. O envio só ocorre quando você o confirma no Gmail. O serviço segue a política de privacidade do Google. As informações enviadas por e-mail serão utilizadas para responder ao seu contato.</p><p>Links para plataformas externas seguem as políticas de privacidade dessas plataformas.</p></div>')
    page('cookies.html','Cookies',intro('Cookies') + '<div class="prose"><p>Esta versão estática do portfólio não utiliza cookies, ferramentas de rastreamento ou armazenamento local. As imagens e estilos são carregados da própria pasta do site.</p><p>Ao acessar links externos, consulte a política de cookies do respectivo serviço.</p></div>')
    print('13 páginas HTML geradas com sucesso.')

if __name__ == '__main__':
    build()
