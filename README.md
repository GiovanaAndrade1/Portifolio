# Portfólio — Giovana Andrade

Portfólio profissional em HTML, CSS e JavaScript.

## Abrir

Dê dois cliques em `index.html`. Todas as páginas e imagens funcionam diretamente, sem instalar bibliotecas ou iniciar servidor.

Para desenvolvimento, opcionalmente execute nesta pasta:

```powershell
python -m http.server 5500 --bind 127.0.0.1
```

Acesse http://127.0.0.1:5500 no seu navegador.

## Organização

- `index.html`: página inicial.
- `sobre.html`, `projetos.html`, `stack.html`, `contato.html`: páginas principais.
- `projetos/`: seis páginas de detalhes.
- `assets/css/styles.css`: estilos organizados em seções; cores, fontes e dimensões em variáveis no início.
- `assets/js/main.js`: menu acessível e preparação do e-mail de contato.
- `assets/images/`: foto e imagens dos projetos salvas localmente.
- `assets/icons/`: ícones locais; ícones indisponíveis na origem foram representados por iniciais.
- `content/site.json`: fonte centralizada dos textos, contatos, experiências, tecnologias e projetos.
- `scripts/build.py`: gerador opcional dos arquivos HTML; usa apenas a biblioteca padrão do Python 3.12+.
- `privacidade.html`, `cookies.html`: textos específicos para esta implementação estática.

## Manutenção

1. Altere os textos e links em `content/site.json`.
2. Execute `python scripts/build.py` dentro desta pasta para atualizar todos os HTMLs.
3. Edite `assets/css/styles.css` para mudar a aparência e `assets/js/main.js` para mudar o comportamento.

Para alterar a estrutura compartilhada (menu, rodapé e marcação), edite `scripts/build.py` e gere novamente. Também é possível editar os HTMLs diretamente, mas uma nova geração substituirá essas edições.

Para adicionar um projeto, inclua um objeto em `projects` no JSON com `slug`, `category`, `title`, `image`, `url` e `body`; salve a imagem em `assets/images/`. Cada item de `body` contém `tag` (`h2`, `h3` ou `p`) e `text`. Gere os HTMLs novamente. Os cartões e a página serão criados automaticamente.

## Formulário

O formulário valida os campos e abre o Gmail no navegador, em outra aba, com destinatário, assunto e mensagem preenchidos. O visitante precisa entrar na conta, se necessário, revisar e clicar em Enviar no Gmail. Não existe servidor de envio ou integração com o formulário do Framer. Para envio direto pela página, será necessário integrar um serviço ou backend.

## Características

- Layout responsivo com navegação lateral no desktop e menu expansível no celular.
- Conteúdo estático visível sem JavaScript; navegação também disponível nesse modo.
- Imagens locais; sem frameworks, instalação de pacotes, rastreadores ou cookies.
- Links de contato abrem a composição de mensagem no Gmail pelo navegador.
- O projeto NaCarteira não tinha endereço externo disponível; seu botão direciona ao contato.
- O projeto de portfólio aponta para o site original.
- Revise as páginas de privacidade e cookies ao adicionar serviços de terceiros.
- Tipografia e ícones utilizam recursos locais.

## Publicação futura

Publique os HTMLs, `projetos/` e `assets/` em qualquer hospedagem estática. `content/` e `scripts/` são arquivos de manutenção e podem ficar fora da publicação. 
