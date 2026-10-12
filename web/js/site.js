const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".nav");

function setMenu(open) {
  nav.classList.toggle("open", open);
  document.body.classList.toggle("menu-open", open);
  toggle.setAttribute("aria-expanded", open ? "true" : "false");
  toggle.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
}

if (toggle && nav) {
  toggle.setAttribute("aria-label", "Ouvrir le menu");
  toggle.addEventListener("click", () => {
    setMenu(!nav.classList.contains("open"));
  });
  document.addEventListener("click", (event) => {
    if (!nav.classList.contains("open")) return;
    if (nav.contains(event.target) || toggle.contains(event.target)) return;
    setMenu(false);
  });
  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      if (link.getAttribute("href").includes("#")) setMenu(false);
    });
  });
}

document.querySelectorAll(".drop > button").forEach((button) => {
  button.addEventListener("click", () => {
    const drop = button.parentElement;
    const willOpen = !drop.classList.contains("open");
    document.querySelectorAll(".drop.open").forEach((other) => {
      if (other === drop) return;
      other.classList.remove("open");
      other.querySelector("button").setAttribute("aria-expanded", "false");
    });
    drop.classList.toggle("open", willOpen);
    button.setAttribute("aria-expanded", willOpen ? "true" : "false");
  });
});

document.querySelectorAll(".gallery-set .more").forEach((button) => {
  const extra = button.previousElementSibling;
  button.addEventListener("click", () => {
    const open = button.getAttribute("aria-expanded") === "true";
    extra.hidden = open;
    button.setAttribute("aria-expanded", open ? "false" : "true");
    button.textContent = open ? button.dataset.open : button.dataset.close;
  });
});

const lightbox = document.querySelector(".lightbox");
const lightboxImg = lightbox.querySelector("img");
const closeBtn = lightbox.querySelector(".lightbox-close");

function closeLightbox() {
  lightbox.classList.remove("open");
  lightboxImg.removeAttribute("src");
}

document.querySelectorAll("[data-full]").forEach((button) => {
  button.addEventListener("click", () => {
    lightboxImg.src = button.dataset.full;
    lightboxImg.alt = button.querySelector("img")?.alt || "";
    lightbox.classList.add("open");
  });
});

closeBtn.addEventListener("click", closeLightbox);
lightbox.addEventListener("click", (event) => {
  if (event.target === lightbox) closeLightbox();
});
document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  closeLightbox();
  if (toggle && nav) setMenu(false);
});
