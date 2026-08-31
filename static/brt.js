function handleRegister(select) {
  const url = select.value;
  if (url) {
    window.location.href = url;
  }
}

function handleLogin(select) {
  const url = select.value;
  if (url) {
    window.location.href = url;
  }
}
document.getElementById("startBtn").addEventListener("click", function () {
  fetch("/start_test")
    .then((res) => res.text())
    .then((data) => {
      window.location.href = "/informtion";
    });
});

document.addEventListener("DOMContentLoaded", function () {
  /* =========================================
       1. Smooth Scroll
    ========================================= */

  const links = document.querySelectorAll('.nav1 a[href^="#"]');

  links.forEach((link) => {
    link.addEventListener("click", function (e) {
      const id = this.getAttribute("href");
      const section = document.querySelector(id);

      if (section) {
        e.preventDefault();

        section.scrollIntoView({
          behavior: "smooth",
        });
      }
    });
  });

  /* =========================================
       2. Header Animation on Scroll
    ========================================= */

  const header = document.getElementById("header");

  window.addEventListener("scroll", function () {
    if (window.scrollY > 80) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  });

  /* =========================================
       3. Start Button Animation
    ========================================= */

  const startBtn = document.getElementById("startBtn");

  if (startBtn) {
    startBtn.addEventListener("mouseenter", function () {
      this.classList.add("button-hover");
    });

    startBtn.addEventListener("mouseleave", function () {
      this.classList.remove("button-hover");
    });

    startBtn.addEventListener("click", function () {
      this.classList.add("button-click");

      setTimeout(() => {
        this.classList.remove("button-click");
      }, 250);
    });
  }

  /* =========================================
       4. Scroll Reveal Animation
    ========================================= */

  const revealElements = document.querySelectorAll(
    ".Beneficiaries1, .About1, .feedback-card, .footer-col",
  );

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-show");

          revealObserver.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.15,
    },
  );

  revealElements.forEach((element, index) => {
    element.style.setProperty("--delay", `${index * 0.12}s`);

    revealObserver.observe(element);
  });

  /* =========================================
       5. Counter Animation
    ========================================= */

  const counter = document.getElementById("counter1");

  if (counter) {
    const finalNumber = parseInt(counter.textContent) || 0;

    counter.textContent = "0";

    let started = false;

    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && !started) {
          started = true;

          let current = 0;
          const duration = 1800;
          const startTime = performance.now();

          function updateCounter(time) {
            const progress = Math.min((time - startTime) / duration, 1);

            // حركة ناعمة
            const ease = 1 - Math.pow(1 - progress, 3);

            current = Math.floor(finalNumber * ease);

            counter.textContent = current;

            if (progress < 1) {
              requestAnimationFrame(updateCounter);
            } else {
              counter.textContent = finalNumber;
            }
          }

          requestAnimationFrame(updateCounter);
        }
      });
    });

    counterObserver.observe(counter);
  }

  /* =========================================
       6. Floating Images
    ========================================= */

  const images = document.querySelectorAll(".About2 img, .Beneficiaries1 img");

  images.forEach((img, index) => {
    img.style.animationDelay = `${index * 0.2}s`;
  });

  /* =========================================
       7. Cards Tilt Effect
    ========================================= */

  const cards = document.querySelectorAll(".Beneficiaries1, .feedback-card");

  cards.forEach((card) => {
    card.addEventListener("mousemove", function (e) {
      // نوقف التأثير على الشاشات الصغيرة
      if (window.innerWidth < 768) return;

      const rect = this.getBoundingClientRect();

      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -5;

      const rotateY = ((x - centerX) / centerX) * 5;

      this.style.transform = `perspective(800px)
                 rotateX(${rotateX}deg)
                 rotateY(${rotateY}deg)
                 translateY(-8px)`;
    });

    card.addEventListener("mouseleave", function () {
      this.style.transform = "";
    });
  });


  /* =========================================
       9. Back To Top
    ========================================= */

  const topButton = document.createElement("button");

  topButton.id = "topButton";
  topButton.innerHTML = "↑";
  topButton.setAttribute("aria-label", "العودة إلى الأعلى");

  document.body.appendChild(topButton);

  window.addEventListener("scroll", function () {
    if (window.scrollY > 400) {
      topButton.classList.add("active");
    } else {
      topButton.classList.remove("active");
    }
  });

  topButton.addEventListener("click", function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  /* =========================================
       10. Active Navigation Link
    ========================================= */

  const sections = document.querySelectorAll(
    "#Home, #Beneficiaries, #About, #feedback, #contact",
  );

  const navItems = document.querySelectorAll(".nav1 li a");

  window.addEventListener("scroll", function () {
    let currentSection = "";

    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 150;

      if (window.scrollY >= sectionTop) {
        currentSection = section.getAttribute("id");
      }
    });

    navItems.forEach((link) => {
      link.classList.remove("active-link");

      const href = link.getAttribute("href");

      if (href === "#" + currentSection) {
        link.classList.add("active-link");
      }
    });
  });

  /* =========================================
       11. Welcome Animation
    ========================================= */

  const homeTitle = document.querySelector("#Home .home1 h1");

  const homeText = document.querySelector("#Home .home1 p");

  if (homeTitle) {
    homeTitle.classList.add("home-title-animation");
  }

  if (homeText) {
    homeText.classList.add("home-text-animation");
  }

  /* =========================================
       12. Disable animations if user prefers
           reduced motion
    ========================================= */

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.documentElement.classList.add("reduce-motion");
  }
});
