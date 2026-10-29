// Tema, filtros da grella e comentarios

(() => {
  const raiz = document.documentElement;
  const escuroDoSistema = window.matchMedia("(prefers-color-scheme: dark)");
  const temaActual = () => raiz.dataset.theme || (escuroDoSistema.matches ? "dark" : "light");

  // ---------- Tema ----------
  document.querySelectorAll("[data-cambiar-tema]").forEach((boton) => {
    boton.addEventListener("click", () => {
      const novo = temaActual() === "dark" ? "light" : "dark";
      raiz.dataset.theme = novo;
      try { localStorage.setItem("tema", novo); } catch (e) {}
      avisarGiscus();
    });
  });
  escuroDoSistema.addEventListener("change", () => { if (!raiz.dataset.theme) avisarGiscus(); });

  // ---------- Filtros ----------
  const filtros = document.querySelector("[data-filtros]");
  const grella = document.querySelector("[data-grella]");
  if (filtros && grella) {
    const chips = filtros.querySelectorAll("[data-sistema]");
    const soProbadas = filtros.querySelector("[data-so-probadas]");
    const baleiro = document.querySelector("[data-baleiro]");
    let sistema = "";
    const aplicar = () => {
      let visibles = 0;
      grella.querySelectorAll(".tarxeta").forEach((t) => {
        const ok = (!sistema || t.dataset.sistema === sistema) && (!soProbadas.checked || t.dataset.probada === "si");
        t.hidden = !ok;
        if (ok) visibles++;
      });
      if (baleiro) baleiro.hidden = visibles > 0;
    };
    chips.forEach((chip) => chip.addEventListener("click", () => {
      sistema = chip.dataset.sistema;
      chips.forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
      aplicar();
    }));
    soProbadas.addEventListener("change", aplicar);
  }

  // ---------- Escaparate da portada ----------
  // Pasa polas capturas en galego de todas as fichas. Párase co rato enriba, co foco dentro ou
  // coa lapela agochada; se o sistema pide menos movemento, só cambia cos puntos.
  const escaparate = document.querySelector("[data-escaparate]");
  if (escaparate) {
    const diapos = [...escaparate.querySelectorAll("[data-diapo]")];
    const puntos = escaparate.querySelector("[data-puntos]");
    const quieto = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const DURACION = 6500, ORIXINAL = 1800;
    const motivos = new Set();
    let actual = 0, temporizador = null, volta = null;

    const amosar = (i) => {
      clearTimeout(volta);
      diapos[actual].classList.remove("activa", "amosa-orixinal");
      actual = (i + diapos.length) % diapos.length;
      const d = diapos[actual];
      d.classList.add("activa");
      diapos.forEach((x, j) => {
        x.setAttribute("aria-hidden", String(j !== actual));
        x.tabIndex = j === actual ? 0 : -1;
      });
      botons.forEach((b, j) => b.setAttribute("aria-current", String(j === actual)));
      if (!quieto && d.classList.contains("con-orixinal")) {
        d.classList.add("amosa-orixinal");
        volta = setTimeout(() => d.classList.remove("amosa-orixinal"), ORIXINAL);
      }
    };
    const programar = () => {
      clearInterval(temporizador);
      if (!quieto && !motivos.size && diapos.length > 1) temporizador = setInterval(() => amosar(actual + 1), DURACION);
    };
    const parar = (motivo, si) => { if (si) motivos.add(motivo); else motivos.delete(motivo); programar(); };

    const botons = diapos.map((d, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", `Ver ${d.dataset.titulo} (${i + 1} de ${diapos.length})`);
      b.addEventListener("click", () => { amosar(i); programar(); });
      puntos.append(b);
      return b;
    });
    puntos.hidden = diapos.length < 2;
    diapos.forEach((d) => { d.hidden = false; });
    escaparate.dataset.listo = "";
    escaparate.addEventListener("mouseenter", () => parar("rato", true));
    escaparate.addEventListener("mouseleave", () => parar("rato", false));
    escaparate.addEventListener("focusin", () => parar("foco", true));
    escaparate.addEventListener("focusout", () => parar("foco", false));
    document.addEventListener("visibilitychange", () => parar("agochada", document.hidden));
    amosar(0);
    programar();
  }

  // ---------- Comentarios (giscus) ----------
  const caixaGiscus = document.querySelector("[data-giscus]");
  const temaGiscus = () => (temaActual() === "dark" ? "dark_dimmed" : "light");
  function avisarGiscus() {
    const marco = document.querySelector("iframe.giscus-frame");
    if (marco) marco.contentWindow.postMessage({ giscus: { setConfig: { theme: temaGiscus() } } }, "https://giscus.app");
  }
  if (caixaGiscus) {
    const d = caixaGiscus.dataset;
    const s = document.createElement("script");
    s.src = "https://giscus.app/client.js";
    s.async = true;
    s.crossOrigin = "anonymous";
    const atributos = {
      "data-repo": d.repo,
      "data-repo-id": d.repoId,
      "data-category": d.category,
      "data-category-id": d.categoryId,
      "data-mapping": "specific",
      "data-term": d.term,
      "data-strict": "1",
      "data-reactions-enabled": "1",
      "data-emit-metadata": "0",
      "data-input-position": "top",
      "data-theme": temaGiscus(),
      "data-lang": d.lang,
      "data-loading": "lazy",
    };
    Object.entries(atributos).forEach(([k, v]) => s.setAttribute(k, v));
    caixaGiscus.appendChild(s);
  }
})();
