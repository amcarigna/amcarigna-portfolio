const header = document.querySelector("header");
const menuBtn = document.querySelector("#menuBtn");
const openIcon = document.querySelector("#openIcon");
const closeIcon = document.querySelector("#closeIcon");
const mobileNav = document.querySelector("#mobileNav");
const mobileLinks = mobileNav.querySelectorAll("a");

function toggleMenu() {
  const isExpanded = menuBtn.getAttribute("aria-expanded") === "true";

  menuBtn.setAttribute("aria-expanded", !isExpanded);

  mobileNav.setAttribute("aria-hidden", isExpanded);

  if (!isExpanded) {
    closeIcon.style.display = "block";
    openIcon.style.display = "none";
    header.style.overflow = "visible";
    mobileNav.classList.add("open");
  } else {
    closeIcon.style.display = "none";
    openIcon.style.display = "block";
    header.style.overflow = "hidden";
    mobileNav.classList.remove("open");
  }
}

menuBtn.addEventListener("click", () => {
  toggleMenu();
});

mobileLinks.forEach((link) => {
  link.addEventListener("click", () => {
    if (mobileNav.classList.contains("open")) {
      toggleMenu();
    }
  });
});

document.querySelectorAll('.filter-btn').forEach(button => {
    button.addEventListener('click', () => {
        const filter = button.dataset.filter;

        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        button.classList.add('active');

        document.querySelectorAll('.project-container').forEach(project => {
            const techs = project.dataset.techs.split(',');
            if (filter === 'all' || techs.includes(filter)) {
                project.style.display = '';
            } else {
                project.style.display = 'none';
            }
        });
    });
});
