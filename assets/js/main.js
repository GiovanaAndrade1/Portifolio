function initializeMenu() {
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.querySelector('#navegacao');
  if (!toggle || !panel) return;

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.querySelector('.sr-only').textContent = open ? 'Fechar menu' : 'Abrir menu';
    panel.classList.toggle('is-open', open);
  }

  toggle.addEventListener('click', () => {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  panel.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
}

function initializeContactForm() {
  const form = document.querySelector('#contact-form');
  if (!form) return;

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const fields = new FormData(form);
    const name = String(fields.get('nome')).trim();
    const email = String(fields.get('email')).trim();
    const message = String(fields.get('mensagem')).trim();
    if (!name || !message) {
      document.querySelector('#form-status').textContent = 'Preencha seu nome e sua mensagem.';
      return;
    }
    const subject = encodeURIComponent(`Contato pelo portfólio — ${name}`);
    const body = encodeURIComponent(`Nome: ${name}\nE-mail: ${email}\n\n${message}`);
    const recipient = encodeURIComponent(form.dataset.email);
    const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${recipient}&su=${subject}&body=${body}`;
    window.open(gmailUrl, '_blank', 'noopener,noreferrer');
    document.querySelector('#form-status').textContent =
      `Revise a mensagem na aba do Gmail e clique em Enviar. Se a aba não abrir, permita pop-ups para este site ou escreva para ${form.dataset.email}.`;
  });
}

initializeMenu();
initializeContactForm();
